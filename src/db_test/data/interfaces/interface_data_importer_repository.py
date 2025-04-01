from abc import ABC, abstractmethod
from typing import Tuple, List, Dict
from decimal import Decimal

class InterfaceDateImporterRepository(ABC):
    @abstractmethod
    def _convert_decimal(self, value: str) -> Decimal: pass

    @abstractmethod
    def _process_csv_file(self, file_path: str) -> Tuple[List[dict], int]: pass

    @abstractmethod
    def process_csv_directory(self, directory_path: str) -> Dict: pass