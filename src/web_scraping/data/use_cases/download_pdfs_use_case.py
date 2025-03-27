from typing import Dict
from pathlib import Path
from src.web_scraping.domain.interfaces.interface_download_pdfs import InterfaceDownloadPdfs
from src.web_scraping.data.interfaces.interface_download_pdfs_repository import InterfaceDownloadPdfsRepository

class DownloadPdfsUseCase(InterfaceDownloadPdfs):
    def __init__(self, repository: InterfaceDownloadPdfsRepository):
        self.repository = repository


    def download_pdfs(self, url: str, diretorio_destino: str, headers: str) -> Dict:

        self.__diretorio_exists(diretorio_destino)

        files_exists = self.__verificar_arquivos(diretorio_destino)

        if files_exists:
            return {
                'message': 'Os arquivos já estão presentes no diretório',
                'data': files_exists
            }

        downloads_files = self.repository.download_pdfs(url, diretorio_destino, headers)

        return self.__result(downloads_files)
    
    @classmethod
    def __diretorio_exists(cls, diretorio_destino: str) -> None:
        # Garante que o diretório de destino existe
        Path(diretorio_destino).mkdir(parents=True, exist_ok=True)

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
        

    @classmethod
    def __result(cls, result: Dict) -> Dict:
          return {
                'message': 'Downloads concluídos com sucesso',
                'data': {
                    'anexo_i': result.get('Anexo I', {}),
                    'anexo_ii': result.get('Anexo II', {})
                }
            }