from abc import ABC, abstractmethod
from typing import Dict

class InterfaceDownloadPdfs(ABC):

    @abstractmethod
    def download_pdfs(self, url: str, diretorio_destino: str, headers: str) -> Dict: pass