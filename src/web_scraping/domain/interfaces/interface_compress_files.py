from abc import ABC, abstractmethod
from typing import Dict

class InterfaceCompressFilesRepository(ABC):
    @abstractmethod
    def compress_files_zip(self, diretorio_destino: str, nome_zip: str, diretorio_origem: str) -> Dict: pass 