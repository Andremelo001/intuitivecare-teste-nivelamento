from src.web_scraping.infra.repositories.compress_files_repository import CompressFilesRepository
from src.web_scraping.data.use_cases.compress_files_use_case import CompressFilesUseCase

class ControllerCompress:
    def run(self, diretorio_destino: str, name_zip: str, diretorio_origem: str):
        try: 
            repository = CompressFilesRepository()

            use_case = CompressFilesUseCase(repository)

            result = use_case.compress_files_zip(diretorio_destino, name_zip, diretorio_origem)
            print(result)
        except Exception as e:
            print(f"Falha: {str(e)}")
            raise