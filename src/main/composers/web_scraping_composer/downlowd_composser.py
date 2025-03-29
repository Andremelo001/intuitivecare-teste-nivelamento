from src.web_scraping.infra.repositories.download_pdfs_repository import DownloadPdfsRepository
from src.web_scraping.data.use_cases.download_pdfs_use_case import DownloadPdfsUseCase
from src.web_scraping.presentation.controllers.controller_download import ControllerDownload

from src.web_scraping.presentation.http_types.http_request import HttpRequest

def download_composser(http_request: HttpRequest):
    repository = DownloadPdfsRepository()

    use_case = DownloadPdfsUseCase(repository)

    controller = ControllerDownload(use_case)

    return controller.handle(http_request)
