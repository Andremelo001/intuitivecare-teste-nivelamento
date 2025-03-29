from src.data_transformation.infra.repositories.extract_tables_repository import ExtractTablesRepository
from src.data_transformation.data.use_cases.extract_tables_use_case import ExtractTablesUseCase
from src.data_transformation.presentation.controllers.controller_extract import ControllerExtract

from src.data_transformation.presentation.http_types.http_request import HttpRequest

def extract_composser(http_request: HttpRequest):
    repository = ExtractTablesRepository()

    use_case = ExtractTablesUseCase(repository)

    controller = ControllerExtract(use_case)

    return controller.handle(http_request)