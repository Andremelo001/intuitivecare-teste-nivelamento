from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from typing import Dict

#Import Adapters
from src.main.adapters.request_adapter import request_adapter

#Import Composers
from src.main.composers.web_scraping_composer.downlowd_composser import download_composser
from src.main.composers.web_scraping_composer.compress_composser import compress_composser


router = APIRouter(
    prefix="/web_scraping",
    tags=["Web_scraping"],
)

@router.post("/download", response_model=Dict)
async def create_client(request: Request):

    http_response = await request_adapter(request, download_composser)

    return JSONResponse(content=http_response.body, status_code=http_response.status_code)

@router.post("/compress", response_model=Dict)
async def create_client(request: Request):

    http_response = await request_adapter(request, compress_composser)

    return JSONResponse(content=http_response.body, status_code=http_response.status_code)


