from src.web_scraping.infra.repositories.download_pdfs_repository import DownloadPdfsRepository
from src.web_scraping.data.use_cases.download_pdfs_use_case import DownloadPdfsUseCase


# URL e diretório de destino
url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
diretorio_destino = "anexos_ans"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Instanciar o repositório e o caso de uso
repository_download = DownloadPdfsRepository()
use_case = DownloadPdfsUseCase(repository_download)


# Executar o download
resultado = use_case.download_pdfs(url, diretorio_destino, headers)
print(resultado)
