from src.data_transformation.presentation.http_types.http_request import HttpRequest
from src.data_transformation.presentation.http_types.http_response import HttpResponse
from src.data_transformation.domain.interfaces.interface_extract_tables_use_case import InterfaceExtractTablesUseCase
from src.data_transformation.presentation.interfaces.controller_interface import ControllerInterface

class ControllerExtract(ControllerInterface):
    def __init__(self, use_case: InterfaceExtractTablesUseCase):
        self.use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        pdf_path = http_request.body.get("pdf_path")
        output_path = http_request.body.get("output_path")

        response = self.use_case.extract_tables(pdf_path, output_path)

        return HttpResponse(
             status_code=200,
             body= {
                 "data": response
             }
         )

