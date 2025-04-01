from src.db_test.data.interfaces.interface_list_operadoras_ultimo_ano_repository import InterfaceListOperadorasUltimoAnoRepository
from src.db_test.domain.interfaces.interface_list_operadoras_ultimo_ano_use_case import InterfaceListOperadorasUltimoAnoUseCase
from typing import Dict
from decimal import Decimal

class ListOperadorasUltimoAnoUseCase(InterfaceListOperadorasUltimoAnoUseCase):
    def __init__(self, repository: InterfaceListOperadorasUltimoAnoRepository):
        self.repository = repository

    def list_operadoras(self) -> Dict:

        return self.__format_reponse()

    
    def __format_reponse(self) -> Dict:
        raw_data = self.repository.top_operadoras_ultimo_ano()
        
        # Formata os resultados corretamente
        operadoras = []
        for index, item in enumerate(raw_data, start=1):
            # Acessa os elementos da tupla pelo índice ou pelo nome do label
            operadora = {
                "nome": item[0],  # ou item.operadora se usou .label()
                "registro_ans": item[1],  # ou item.registro_ans
                "total_despesas": float(item[2]) if isinstance(item[2], Decimal) else float(0),
                "quantidade_registros": item[3],  # quantidade_registros
                "posicao_ranking": index
            }
            operadoras.append(operadora)
        
        return {
            "operadoras": operadoras
        }

        
