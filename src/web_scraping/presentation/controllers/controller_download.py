from src.web_scraping.domain.interfaces.interface_download_pdfs import InterfaceDownloadPdfs
from src.web_scraping.presentation.interfaces.controller_interface import ControllerInterface
from src.web_scraping.presentation.http_types.http_request import HttpRequest
from src.web_scraping.presentation.http_types.http_response import HttpResponse

class ControllerDownload(ControllerInterface):
    def __init__(self, use_case: InterfaceDownloadPdfs):
        self.use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        url = http_request.body.get("url")  # Usa .get() para evitar KeyError
        diretorio_destino = http_request.body.get("diretorio_destino")
        headers = http_request.body.get("headers")

        response = self.use_case.download_pdfs(url, diretorio_destino, headers)

        return HttpResponse(
             status_code=200,
             body= {
                 "data": response
             }
         )