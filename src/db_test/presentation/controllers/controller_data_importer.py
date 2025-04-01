from src.db_test.presentation.http_types.http_request import HttpRequest
from src.db_test.presentation.http_types.http_response import HttpResponse
from src.db_test.presentation.interfaces.controller_interface import ControllerInterface
from src.db_test.domain.interfaces.interface_data_importer_use_case import InterfaceDataImporterUseCase

class ControllerDataImporter(ControllerInterface):
    def __init__(self, use_case: InterfaceDataImporterUseCase):
        self.use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        directory_path = http_request.body.get("file_path")

        response = self.use_case.process_csv(directory_path)

        return HttpResponse(
             status_code=200,
             body= {
                 "data": response
             }
         )

