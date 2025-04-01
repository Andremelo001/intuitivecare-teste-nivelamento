from abc import ABC, abstractmethod
from src.data_transformation.presentation.http_types.http_request import HttpRequest
from src.data_transformation.presentation.http_types.http_response import HttpResponse


class ControllerInterface(ABC):

    @abstractmethod
    def handle(self, http_request: HttpRequest) -> HttpResponse: pass


