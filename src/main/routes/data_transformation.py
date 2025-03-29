from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from typing import Dict

#Import Adapters
from src.main.adapters.request_adapter import request_adapter

#Import Composers
from src.main.composers.data_transformation_composer.extract_composser import extract_composser
from src.main.composers.web_scraping_composer.compress_composser import compress_composser


router = APIRouter(
    prefix="/data_transformation",
    tags=["Data_transformation"],
)

@router.post("/extract_and_save_csv", response_model=Dict)
async def create_client(request: Request):

    http_response = await request_adapter(request, extract_composser)

    return JSONResponse(content=http_response.body, status_code=http_response.status_code)

@router.post("/csv_compress_zip", response_model=Dict)
async def create_client(request: Request):

    http_response = await request_adapter(request, compress_composser)

    return JSONResponse(content=http_response.body, status_code=http_response.status_code)



