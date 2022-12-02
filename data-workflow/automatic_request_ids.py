from datetime import datetime
from sqlalchemy import create_engine, text
from httplib2 import Http
import json
import uuid
import re

from airflow import DAG

from airflow.operators.python import PythonOperator

def _http_request_salic(offset, url):
    http_options = {
        "base_url": "api.salic.cultura.gov.br/v1",
        "limit": "500",
        "tipo_pessoa": "juridica",
        "format": "json"
            }
    salic_url = "http://" + http_options["base_url"] + url + "/?limit=" + http_options["limit"] + "&offset=" + offset + "&tipo_pessoa=" + http_options["tipo_pessoa"] + "&format=" + http_options["format"]
    print("[REQUESTED URL]: " + salic_url)
    http_obj = Http()
    response = http_obj.request(salic_url, method="GET")[1]
    json_res = json.loads(response.decode())
    return json_res

def _extract_sponsor_id_salic(full_text):
    remove_pattern = "http://api.salic.cultura.gov.br/v1/incentivadores/"
    return re.sub(remove_pattern, '', full_text)

def _record_sponsor_database(sponsor_list):
    database_url="postgresql://postgres:changeme@172.17.0.1:5432/postgres"
    engine=create_engine(database_url)
    for sponsor in sponsor_list:
#        sponsor_id = uuid.uuid4()
        sponsor_name = sponsor["nome"]
        sponsor_cgccpf = sponsor["cgccpf"]
        sponsor_tipo = sponsor["tipo_pessoa"]
        sponsor_responsavel = sponsor["responsavel"]
        sponsor_total_doado = str(sponsor["total_doado"])
        sponsor_uf = sponsor["UF"]
        sponsor_municipio = sponsor["municipio"]

        sponsor_with_id = sponsor["_links"]["self"]
        id_sponsor = _extract_sponsor_id_salic(sponsor_with_id)

        engine.execute(text("INSERT INTO sponsor_salic(id_sponsor_salic, sponsor_name, cgccpf, tipo_pessoa, responsavel, total_doado, uf, municipio) VALUES (:id_sponsor_salic, :sponsor_name, :cgccpf, :tipo_pessoa, :responsavel, :total_doado, :uf, :municipio)"), {"id_sponsor_salic": id_sponsor, "sponsor_name": sponsor_name, "cgccpf": sponsor_cgccpf, "tipo_pessoa": sponsor_tipo, "responsavel": sponsor_responsavel, "total_doado": sponsor_total_doado, "uf": sponsor_uf, "municipio": sponsor_municipio})

def _create_new_request(last_offset):
    database_url="postgresql://postgres:changeme@172.17.0.1:5432/postgres"
    engine=create_engine(database_url)

    nr_id = uuid.uuid4()
    nr_status = "pending"
    nr_query_limit = "500"

    if int(last_offset) == 18000:
        nr_offset = 18220
    else: 
        nr_offset = int(last_offset) + int(500)
    
    total_items = "18220"

    engine.execute(text("INSERT INTO http_request_metadata(request_id, status, query_limit, query_offset, total_items) VALUES(:request_id, :status, :query_limit, :query_offset, :total_items)"), {"request_id": nr_id, "status": nr_status, "query_limit": nr_query_limit, "query_offset": nr_offset, "total_items": total_items})


def _update_request_status(current_id, request_status):
    database_url="postgresql://postgres:changeme@172.17.0.1:5432/postgres"
    engine=create_engine(database_url)
    table_name="http_request_metadata"
    update_status = engine.execute(text(f"UPDATE {table_name} " f"SET {request_status} " f"WHERE request_id='{current_id}'"))

def _main():
    database_url="postgresql://postgres:changeme@172.17.0.1:5432/postgres"
    engine=create_engine(database_url)

    database_request_ids = engine.execute(text("SELECT * FROM http_request_metadata"))
    
    for process_request in database_request_ids:
        if process_request["status"] == "pending":
            print("[SALIC_REQUEST]")
            sponsor_list_salic = _http_request_salic(process_request["query_offset"], "/incentivadores")["_embedded"]["incentivadores"]

            print("[SAVE_DATA_IN_DATABASE]]")
            _record_sponsor_database(sponsor_list_salic)
            
            print("[UPDATE_REQUEST_TABLE_PROPS - STATUS TO DONE]")
            _update_request_status(process_request["request_id"], "status='done'")
            
            print("[CRETE_NEW_REQUEST - NEW ID, STATUS PENDING]")
            _create_new_request(process_request["query_offset"])
        elif(process_request["status"] == "done"):
            print("[NO MORE REQUESTS_TO_PROCESS]")


default_args = {
    'start_date': datetime(2022, 12, 1)
}

with DAG('process_requests_automatically_second', schedule_interval='*/5 * * * *',
        default_args=default_args,
        catchup=False) as dag:

    request_salic_api = PythonOperator(
            task_id="request_salic_api",
            python_callable=_main
    )

request_salic_api


