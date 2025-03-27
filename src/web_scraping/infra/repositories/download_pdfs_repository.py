import requests
from bs4 import BeautifulSoup
import os
from typing import Dict
from src.web_scraping.data.interfaces.interface_download_pdfs_repository import InterfaceDownloadPdfsRepository

class DownloadPdfsRepository(InterfaceDownloadPdfsRepository):
    @classmethod
    def download_pdfs(cls, url: str, diretorio_destino: str, headers: str) -> Dict:
        """ Baixa os Anexos I e II da página da ANS
        
        Args:
            url: URL da página principal
            diretorio_destino: Pasta onde os arquivos serão salvos
            headers: Cabeçalhos HTTP
            
        Returns:
            Dicionário com status e mensagem"""
        try:
            resposta = requests.get(url, headers=headers)
            resposta.raise_for_status()
            
            soup = BeautifulSoup(resposta.text, 'html.parser')

            # Lista de anexos a baixar
            anexos_para_baixar = {
                'Anexo I': 'Anexo_I.pdf',
                'Anexo II': 'Anexo_II.pdf'
            }
            
            resultados = {}
            
            for anexo_nome, arquivo_nome in anexos_para_baixar.items():
                link_pdf = soup.find('a', string=lambda text: text and anexo_nome.lower() in text.lower())

                if link_pdf and 'href' in link_pdf.attrs:
                    href = link_pdf['href']
                    
                    # Resolve URL completa
                    pdf_url = href if href.startswith('http') else f"{url.rsplit('/', 1)[0]}/{href.lstrip('/')}"
                    
                    caminho_completo = os.path.join(diretorio_destino, arquivo_nome)
                    
                    try:
                        # Baixa o PDF
                        resposta_pdf = requests.get(pdf_url, headers=headers, stream=True)
                        resposta_pdf.raise_for_status()
                        
                        with open(caminho_completo, 'wb') as arquivo:
                            for chunk in resposta_pdf.iter_content(chunk_size=8192):
                                arquivo.write(chunk)
                        
                        resultados[anexo_nome] = {
                            'status': 'sucesso',
                            'caminho': caminho_completo,
                            'tamanho': os.path.getsize(caminho_completo)
                        }
                        
                    except Exception as e:
                        resultados[anexo_nome] = {
                            'status': 'erro',
                            'mensagem': str(e)
                        }
                else:
                    resultados[anexo_nome] = {
                        'status': 'erro',
                        'mensagem': f'Link para {anexo_nome} não encontrado na página'
                    }

            return resultados
        
        except Exception as e:
            return {
                'status': 'erro',
                'mensagem': str(e)
            }