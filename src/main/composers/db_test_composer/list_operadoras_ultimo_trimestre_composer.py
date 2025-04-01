from src.db_test.presentation.http_types.http_request import HttpRequest
from src.db_test.infra.repositories.list_operadoras_ultimo_trimestre_repository import ListOperadorasUltimoTrimestreRepository
from src.db_test.data.use_cases.list_operadoras_ultimo_trimestres_use_case import ListOperadorasUltimoTrimestreUseCase
from src.db_test.presentation.controllers.controller_list_operadoras_ultimo_trimestre import ControllerListOperadorasUltimoTrimestre

def list_operadoras_ultimo_trimestre_composer(http_request: HttpRequest):
    
    repository = ListOperadorasUltimoTrimestreRepository()

    use_case = ListOperadorasUltimoTrimestreUseCase(repository)

    controller = ControllerListOperadorasUltimoTrimestre(use_case)

    return controller.handle(http_request)