import os
from src.web_scraping.infra.drivers.shutil_driver import ShutilDriver
from src.web_scraping.data.interfaces.interface_compress_files_repository import InterfaceCompressFilesRepository

class CompressFilesRepository(InterfaceCompressFilesRepository):
    def __init__(self):
        self.shutil_driver = ShutilDriver()

    def compress_files_zip(self, diretorio_destino: str, nome_zip: str, diretorio_origem: str) -> None:
        """
        Compacta arquivos usando o driver ZIP
        
        Args:
            diretorio_destino: Onde o ZIP será salvo
            nome_zip: Nome do arquivo (sem extensão)
            diretorio_origem: Pasta a ser compactada
            
        Raises:
            Exception: Se a compressão falhar
        """
        caminho_zip = os.path.join(diretorio_destino, nome_zip)

        try:
            self.shutil_driver.compress_file(base_name=caminho_zip, root_dir=diretorio_origem)

        except Exception as e:
            raise RuntimeError(f"Erro no repositório: {str(e)}")
        