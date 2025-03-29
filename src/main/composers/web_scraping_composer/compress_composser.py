from src.web_scraping.infra.repositories.compress_files_repository import CompressFilesRepository
from src.web_scraping.data.use_cases.compress_files_use_case import CompressFilesUseCase
from src.web_scraping.presentation.controllers.controller_compress import ControllerCompress

from src.web_scraping.presentation.http_types.http_request import HttpRequest

def compress_composser(http_request: HttpRequest):
    repository = CompressFilesRepository()

    use_case = CompressFilesUseCase(repository)

    controller = ControllerCompress(use_case)

    return controller.handle(http_request)