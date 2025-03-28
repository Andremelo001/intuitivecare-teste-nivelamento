from src.web_scraping.infra.repositories.download_pdfs_repository import DownloadPdfsRepository
from src.web_scraping.data.use_cases.download_pdfs_use_case import DownloadPdfsUseCase

class ControllerDownload:
    def run(self, url: str, diretorio_destino: str, headers: str):
        try: 
            
            repository_download = DownloadPdfsRepository()

            use_case = DownloadPdfsUseCase(repository_download)

            resultado = use_case.download_pdfs(url, diretorio_destino, headers)

            print(resultado)

        except Exception as e:
            print(f"Falha: {str(e)}")
            raise