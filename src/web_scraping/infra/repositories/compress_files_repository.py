import os
import shutil

from src.web_scraping.data.interfaces.interface_compress_files_repository import InterfaceCompressFilesRepository

class CompressFilesRepository(InterfaceCompressFilesRepository):
    @classmethod
    def compress_files_zip(cls, diretorio_destino: str, nome_zip: str, diretorio_origem: str) -> None:
        """    
        Compacta todos os arquivos do diretório em um arquivo ZIP.
        
        :param diretorio_destino: Caminho do diretório onde estão os arquivos.
        :param nome_zip: Nome do arquivo ZIP (sem extensão).
        :return: Caminho do arquivo ZIP criado.
        """    
        caminho_zip = os.path.join(diretorio_destino, nome_zip)
        
        # Criando o ZIP (shutil faz isso automaticamente)
        shutil.make_archive(caminho_zip, 'zip', diretorio_origem)