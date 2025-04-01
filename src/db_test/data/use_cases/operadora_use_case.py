from typing import Dict
import os
from src.db_test.data.interfaces.interface_operadora_repository import InterfaceOperadoraRepository
from src.db_test.domain.interfaces.interface_operadora_use_case import InterfaceOperadoraUseCase

class OperadoraUseCase(InterfaceOperadoraUseCase):
    def __init__(self, repository: InterfaceOperadoraRepository):
        self.repository = repository

    def import_operadoras(self, file_path: str) -> Dict:

        self.__file_exists(file_path)

        return self.repository.import_operadoras_csv(file_path)

    @classmethod
    def __file_exists(cls, caminho_arquivo) -> None:
        """
        Verifica se um arquivo existe no caminho especificado.
        
        Parâmetros:
            caminho_arquivo (str): O caminho completo para o arquivo a ser verificado.
            
        Retorna:
            bool: True se o arquivo existe, False caso contrário.
        """
        if not os.path.isfile(caminho_arquivo):
            raise Exception("Arquivo não encontrado")
