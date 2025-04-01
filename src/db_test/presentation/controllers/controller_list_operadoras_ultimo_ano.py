from src.db_test.presentation.http_types.http_response import HttpResponse
from src.data_transformation.presentation.http_types.http_request import HttpRequest
from src.db_test.presentation.interfaces.controller_interface import ControllerInterface
from src.db_test.domain.interfaces.interface_list_operadoras_ultimo_ano_use_case import InterfaceListOperadorasUltimoAnoUseCase

class ControllerListOperadorasUltimoAno(ControllerInterface):
    def __init__(self, use_case: InterfaceListOperadorasUltimoAnoUseCase):
        self.use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        response = self.use_case.list_operadoras()

        return HttpResponse(
             status_code=200,
             body= {
                 "data": response
             }
         )

