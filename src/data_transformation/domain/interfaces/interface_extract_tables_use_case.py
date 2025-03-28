from abc import ABC, abstractmethod
from typing import List, Dict

class InterfaceExtractTablesUseCase:
    @abstractmethod
    def extract_tables(self, pdf_path: str) -> List[Dict]: pass