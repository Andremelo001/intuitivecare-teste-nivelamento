from src.db_test.infra.repositories.data_importer_repository import DataImporterRepository
from src.db_test.data.use_cases.data_importer_use_case import DataImporterUseCase
from src.db_test.presentation.controllers.controller_data_importer import ControllerDataImporter

from src.db_test.presentation.http_types.http_request import HttpRequest

def data_importer_composer(http_request: HttpRequest):

    repository = DataImporterRepository()

    use_case = DataImporterUseCase(repository)

    controller = ControllerDataImporter(use_case)

    return controller.handle(http_request)