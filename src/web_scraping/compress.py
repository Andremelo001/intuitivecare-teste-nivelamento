from src.web_scraping.infra.repositories.compress_files_repository import CompressFilesRepository
from src.web_scraping.data.use_cases.compress_files_use_case import CompressFilesUseCase

# URL e diretório de destino
diretorio_destino = "zip_anexos_ans"
name_zip = "arquivos_compactados"
diretorio_origem = "anexos_ans"

repository = CompressFilesRepository()

use_case = CompressFilesUseCase(repository)

result = use_case.compress_files_zip(diretorio_destino, name_zip, diretorio_origem)
print(result)
