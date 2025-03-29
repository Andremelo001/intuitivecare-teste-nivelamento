from abc import ABC, abstractmethod
from typing import List, Dict

class InterfacePdfRepository(ABC):
    @abstractmethod
    def extract(self, pdf_path: str) -> List[Dict]: pass
    
    @abstractmethod
    def save_to_csv(self, data: List[Dict], output_path: str) -> str: pass