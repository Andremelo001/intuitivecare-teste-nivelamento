import os
from typing import Dict
from pathlib import Path

from src.web_scraping.data.interfaces.interface_compress_files_repository import InterfaceCompressFilesRepository
from src.web_scraping.domain.interfaces.interface_compress_files import InterfaceCompressFiles


class CompressFilesUseCase(InterfaceCompressFiles):
    def __init__(self, repository: InterfaceCompressFilesRepository):
        self.repository = repository
    
    def compress_files_zip(self, diretorio_destino: str, nome_zip: str, diretorio_origem: str) -> Dict:

        self.__diretorio_exists(diretorio_destino)

        status_files = self.__verificar_arquivos(diretorio_destino)

        if any(status['status'] == 'presente' for status in status_files.values()):
            return {"message": "Arquivo já presente no diretório"}

        zip_exists = self.__zip_exists(diretorio_destino, nome_zip)

        if zip_exists:
            return {"message": "Arquivo zip já existe"}

        self.repository.compress_files_zip(diretorio_destino, nome_zip, diretorio_origem)

        return self.__response(diretorio_destino, nome_zip, diretorio_origem)
    
    @classmethod
    def __zip_exists(cls, diretorio_destino: str, nome_zip: str) -> str:
        caminho_zip = os.path.join(diretorio_destino, nome_zip + ".zip")
    
        # Verifica se o ZIP já existe
        if os.path.exists(caminho_zip):
            return caminho_zip
        
    @classmethod
    def __response(cls, diretorio_destino: str, nome_zip: str, diretorio_origem: str) -> Dict:

        return {
            'message': 'zip criado com sucesso',
            'data': {
                'diretorio': diretorio_destino,
                'zip_name': nome_zip,
                'diretorio_origem': diretorio_origem
            }
        }
    
    @classmethod
    def __diretorio_exists(cls, diretorio_destino: str) -> None:
        # Criando a pasta de destino caso não exista
        os.makedirs(diretorio_destino, exist_ok=True)

    @classmethod
    def __verificar_arquivos(cls, diretorio_destino: str) -> Dict:
        """Verifica se os arquivos já existem no diretório"""
        arquivos = {
            'anexo_i': Path(diretorio_destino) / "Anexo_I.pdf",
            'anexo_ii': Path(diretorio_destino) / "Anexo_II.pdf"
        }

        arquivos_encontrados = {
            chave: {
                'status': 'presente',
                'caminho': str(arquivo.resolve()),
                'tamanho': arquivo.stat().st_size
            }
            for chave, arquivo in arquivos.items() if arquivo.exists()
        }

        return arquivos_encontrados


    
        
        