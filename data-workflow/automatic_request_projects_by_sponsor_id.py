from datetime import datetime
from sqlalchemy import create_engine, text
from httplib2 import Http
import json
import uuid
import re

from airflow import DAG

from airflow.operators.python import PythonOperator

def _http_request_doacoes_por_incentivador_salic(sponsor_id):
    http_options = {
        "base_url": "api.salic.cultura.gov.br/v1",
        "limit": "100",
        "format": "json"
        }
    salic_url = "http://" + http_options["base_url"] + "/incentivadores/" + sponsor_id + "/doacoes" "/?limit=" + http_options["limit"] + "&offset=0" + "&format=" + http_options["format"]
    http_obj = Http()
    response = http_obj.request(salic_url, method="GET")[1]
    json_res = json.loads(response.decode())
    return json_res

def _record_donation_database(sponsor_id_from_db, http_salic_response):
    database_url="postgresql://postgres:docker@172.17.0.1:5433/salic_raw_data"
    engine=create_engine(database_url)

    recibo_salic = http_salic_response["data_recibo"]
    cnpj_salic = http_salic_response["cgccpf"]
    nome_doador_salic = http_salic_response["nome_doador"]
    nome_projeto_salic = http_salic_response["nome_projeto"]
    projeto_salic = http_salic_response["_links"]["projeto"]
    incentivador_salic = http_salic_response["_links"]["incentivador"]
    valor_salic = http_salic_response["valor"]
    pronac_salic = http_salic_response["PRONAC"]
    engine.execute(text("INSERT INTO donations_sponsor_salic(id_sponsor_salic, data_recibo, cgccpf, nome_doador, nome_projeto, projeto_link, incentivador_link, valor, PRONAC) VALUES(:id_sponsor_salic, :data_recibo, :cgccpf, :nome_doador, :nome_projeto, :projeto_link, :incentivador_link, :valor, :PRONAC)"), {"id_sponsor_salic":sponsor_id_from_db, "data_recibo":recibo_salic, "cgccpf":cnpj_salic, "nome_doador":nome_doador_salic, "nome_projeto":nome_projeto_salic, "projeto_link":projeto_salic, "incentivador_link":incentivador_salic, "valor":valor_salic, "PRONAC":pronac_salic})

def _main():
    database_url="postgresql://postgres:docker@172.17.0.1:5433/salic_raw_data"
    engine=create_engine(database_url)
    
    limit_entries = 100
    offset_initial = 0

    sponsor_ids = engine.execute(text("SELECT id_sponsor_salic FROM sponsor_salic  limit :limit offset :offset"), {"limit": limit_entries, "offset": offset_initial})
    for sponsor_id in sponsor_ids:
        response = _http_request_doacoes_por_incentivador_salic(sponsor_id[0])
        doacoes = response["_embedded"]["doacoes"]
        for doacao in doacoes:
            _record_donation_database(sponsor_id[0], doacao)


    
    print("SELECT SPONSOR ID_SPONSOR_SALIC FROM DATABASE")

    print("REQUEST DONATIONS BY SPONSOR ID IN SALIC ENDPOINT")



default_args = {
    'start_date': datetime(2022, 12, 1)
}

with DAG('donations_by_sponsor_id', schedule_interval='@daily',
        default_args=default_args,
        catchup=False) as dag:

    request_salic_api = PythonOperator(
            task_id="request_salic_api",
            python_callable=_main
    )

request_salic_api


