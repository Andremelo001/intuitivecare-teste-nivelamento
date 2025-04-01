from src.data_transformation.presentation.http_types.http_request import HttpRequest
from src.db_test.infra.repositories.list_operadoras_ultimo_ano_repository import ListOperadorasUltimoAnoRepository
from src.db_test.data.use_cases.list_operadoras_ultimo_ano_use_case import ListOperadorasUltimoAnoUseCase
from src.db_test.presentation.controllers.controller_list_operadoras_ultimo_ano import ControllerListOperadorasUltimoAno

def list_operadoras_ultimo_trimestre_ano(http_request: HttpRequest):
    
    repository = ListOperadorasUltimoAnoRepository()

    use_case = ListOperadorasUltimoAnoUseCase(repository)

    controller = ControllerListOperadorasUltimoAno(use_case)

    return controller.handle(http_request)