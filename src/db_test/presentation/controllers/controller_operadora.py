from src.db_test.presentation.http_types.http_request import HttpRequest
from src.db_test.presentation.http_types.http_response import HttpResponse
from src.db_test.presentation.interfaces.controller_interface import ControllerInterface
from src.db_test.domain.interfaces.interface_operadora_use_case import InterfaceOperadoraUseCase

class ControllerOperadora(ControllerInterface):
    def __init__(self, use_case: InterfaceOperadoraUseCase):
        self.use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        file_path = http_request.body.get("file_path")

        response = self.use_case.import_operadoras(file_path)

        return HttpResponse(
             status_code=200,
             body= {
                 "data": response
             }
         )

