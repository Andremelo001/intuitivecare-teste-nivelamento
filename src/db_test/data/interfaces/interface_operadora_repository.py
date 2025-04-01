from abc import ABC, abstractmethod
from typing import Dict

class InterfaceOperadoraRepository(ABC):

    @abstractmethod
    def import_operadoras_csv(self, file_path: str) -> Dict: pass