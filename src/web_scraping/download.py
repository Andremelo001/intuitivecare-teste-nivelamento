from src.web_scraping.presentation.controllers.controller_download import ControllerDownload

if __name__ == "__main__":
    ControllerDownload().run(
        url="https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos",
        diretorio_destino="data/raw",
        headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    )