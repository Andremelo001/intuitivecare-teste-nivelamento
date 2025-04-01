from src.db_test.infra.repositories.operadora_repository import OperadoraRepository
from src.db_test.data.use_cases.operadora_use_case import OperadoraUseCase
from src.db_test.presentation.controllers.controller_operadora import ControllerOperadora
from src.db_test.presentation.http_types.http_request import HttpRequest

def operadora_importer_composer(http_request: HttpRequest):

    repository = OperadoraRepository()

    use_case = OperadoraUseCase(repository)

    controller = ControllerOperadora(use_case)

    return controller.handle(http_request)
