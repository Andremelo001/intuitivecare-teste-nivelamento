from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from typing import Dict

#Import Adapters
from src.main.adapters.request_adapter import request_adapter

#Import Composers
from src.main.composers.db_test_composer.data_importer_composer import data_importer_composer
from src.main.composers.db_test_composer.operadora_importer_composer import operadora_importer_composer
from src.main.composers.db_test_composer.list_operadoras_ultimo_trimestre_composer import list_operadoras_ultimo_trimestre_composer
from src.main.composers.db_test_composer.list_operadoras_ultimo_ano_composer import list_operadoras_ultimo_trimestre_ano


router = APIRouter(
    prefix="/db_test",
    tags=["Db_test"],
)

@router.post("/data_importer_table", response_model=Dict)
async def create_client(request: Request):

    http_response = await request_adapter(request, data_importer_composer)

    return JSONResponse(content=http_response.body, status_code=http_response.status_code)

@router.post("/operadora_importer_table", response_model=Dict)
async def create_client(request: Request):

    http_response = await request_adapter(request, operadora_importer_composer)

    return JSONResponse(content=http_response.body, status_code=http_response.status_code)

@router.get("/list_operadoras_ultimo_trimestre", response_model=Dict)
async def create_client(request: Request):

    http_response = await request_adapter(request, list_operadoras_ultimo_trimestre_composer)

    return JSONResponse(content=http_response.body, status_code=http_response.status_code)

@router.get("/list_operadoras_ultimo_ano", response_model=Dict)
async def create_client(request: Request):

    http_response = await request_adapter(request, list_operadoras_ultimo_trimestre_ano)

    return JSONResponse(content=http_response.body, status_code=http_response.status_code)



