from typing import Dict
import os
from src.db_test.data.interfaces.interface_data_importer_repository import InterfaceDateImporterRepository

class DataImporterUseCase():
    def __init__(self, repository: InterfaceDateImporterRepository):
        self.repository = repository

    def process_csv(self, directory_path: str) -> Dict:

        self.__file_exists(directory_path)
        
        return self.repository.process_csv_directory(directory_path)
    
    @classmethod
    def __file_exists(cls, directory_path: str) -> bool:
        """
        Verifica se um arquivo existe no caminho especificado.
        
        Parâmetros:
            caminho_arquivo (str): O caminho completo para o arquivo a ser verificado.
            
        Retorna:
            bool: True se o arquivo existe, False caso contrário.
        """
        # Verifica se o diretório existe
        if not os.path.isdir(directory_path):
            raise Exception(f"Diretório não encontrado: {directory_path}")
