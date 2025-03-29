import os
from typing import Dict
from src.web_scraping.data.interfaces.interface_download_pdfs_repository import InterfaceDownloadPdfsRepository
from src.web_scraping.infra.drivers.requests_driver import RequestsDriver
from src.web_scraping.infra.drivers.beautifulsoup_driver import BeautifulSoupDriver

class DownloadPdfsRepository(InterfaceDownloadPdfsRepository):
    def __init__(self):
        self.http_driver = RequestsDriver()
        self.html_parser = BeautifulSoupDriver()

    def download_pdfs(self, url: str, diretorio_destino: str, headers: str) -> Dict:
        try:
            # 1. Requisição HTTP
            response = self.http_driver.get(url, headers)
            self.http_driver.validate_response(response)
            
            # 2. Parse HTML
            soup = self.html_parser.parse(response.text)
            
            # 3. Download dos PDFs
            anexos = {
                'Anexo I': 'Anexo_I.pdf',
                'Anexo II': 'Anexo_II.pdf'
            }
            
            resultados = {}
            
            for anexo_nome, arquivo_nome in anexos.items():
                link = self.html_parser.find_link(soup, anexo_nome)
                
                if not link:
                    resultados[anexo_nome] = {'status': 'erro', 'mensagem': f'Link não encontrado'}
                    continue
                    
                pdf_url = self._resolve_url(url, link['href'])
                
                caminho = os.path.join(diretorio_destino, arquivo_nome)
                
                resultados[anexo_nome] = self._download_pdf(pdf_url, caminho, headers)
            
            return resultados
            
        except Exception as e:
            return {'status': 'erro', 'mensagem': str(e)}

    def _resolve_url(self, base_url: str, href: str) -> str:
        return href if href.startswith('http') else f"{base_url.rsplit('/', 1)[0]}/{href.lstrip('/')}"

    def _download_pdf(self, url: str, caminho: str, headers: Dict[str, str]) -> Dict:
        try:
            response = self.http_driver.get(url, headers)
            self.http_driver.validate_response(response)
            
            with open(caminho, 'wb') as arquivo:
                for chunk in response.iter_content(chunk_size=8192):
                    arquivo.write(chunk)
            
            return {
                'status': 'sucesso',
                'caminho': caminho,
                'tamanho': os.path.getsize(caminho)
            }
        except Exception as e:
            return {'status': 'erro', 'mensagem': str(e)}