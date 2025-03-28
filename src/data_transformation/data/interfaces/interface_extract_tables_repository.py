from abc import ABC, abstractmethod
from typing import List

class InterfacePdfRepository(ABC):
    @abstractmethod
    def extract(self, pdf_path: str) -> List[dict]:
        pass