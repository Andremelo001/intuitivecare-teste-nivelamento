from src.web_scraping.domain.interfaces.interface_compress_files import InterfaceCompressFiles
from src.web_scraping.presentation.interfaces.controller_interface import ControllerInterface
from src.web_scraping.presentation.http_types.http_request import HttpRequest
from src.web_scraping.presentation.http_types.http_response import HttpResponse

class ControllerCompress(ControllerInterface):
    def __init__(self, use_case: InterfaceCompressFiles):
        self.use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        diretorio_destino = http_request.body.get("diretorio_destino")
        nome_zip = http_request.body.get("nome_zip")
        diretorio_origem = http_request.body.get("diretorio_origem")

        response = self.use_case.compress_files_zip(diretorio_destino, nome_zip, diretorio_origem)

        return HttpResponse(
             status_code=200,
             body= {
                 "data": response
             }
         )

