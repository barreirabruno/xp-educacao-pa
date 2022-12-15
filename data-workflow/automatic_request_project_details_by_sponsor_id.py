from datetime import datetime
from sqlalchemy import create_engine, text
from httplib2 import Http
import json
import uuid
import re

from airflow import DAG

from airflow.operators.python import PythonOperator

def _http_request_project_by_salic_number(pronac_number):
    http_options = {
        "base_url": "api.salic.cultura.gov.br/v1",
        "format": "json"
        }
    salic_url = "http://" + http_options["base_url"] + "/projetos/" + pronac_number + "?format=" + http_options["format"]
    http_obj = Http()
    response = http_obj.request(salic_url, method="GET")[1]
    json_res = json.loads(response.decode())
    return json_res

def _record_project_sinopse_salic(sponsor_id_salic, response):
    database_url="postgresql://postgres:docker@172.17.0.1:5433/salic_raw_data"
    engine=create_engine(database_url)

    print(sponsor_id_salic)
    if 'message' in response:
        print("PROJECT DATA NOT FOUND, RECORD EMPTY STRINGS ON DATABASE")
        engine.execute(text("INSERT INTO project_area_salic(id_sponsor_salic) VALUES(:id_sponsor_salic)"), {"id_sponsor_salic": sponsor_id_salic})
    else:
        print("PROJECT DATA FOUND, RECORD FULL PROJECT")
        engine.execute(text("INSERT INTO project_area_salic(id_sponsor_salic, nome_projeto, ano_projeto, area, sinopse) VALUES(:id_sponsor_salic, :nome_projeto, :ano_projeto, :area, :sinopse)"), {"id_sponsor_salic": sponsor_id_salic, "nome_projeto": response["nome"], "ano_projeto": response["ano_projeto"], "area": response["area"], "sinopse": response["sinopse"]})
        

def _main():
    database_url="postgresql://postgres:docker@172.17.0.1:5433/salic_raw_data"
    engine=create_engine(database_url)

    limit_entries = 1423
    offset_initial = 0

    sponsor_ids = engine.execute(text("SELECT id_sponsor_salic, pronac FROM donations_sponsor_salic  limit :limit offset :offset"), {"limit": limit_entries, "offset": offset_initial})

    for sponsor in sponsor_ids:
        response = _http_request_project_by_salic_number(sponsor[1])
        _record_project_sinopse_salic(sponsor[0], response)

default_args = {
    'start_date': datetime(2022, 12, 1)
}

with DAG('project_details_by_sponsor_id', schedule_interval='@daily',
        default_args=default_args,
        catchup=False) as dag:

    request_salic_api = PythonOperator(
            task_id="request_salic_api",
            python_callable=_main
    )

request_salic_api


