from typing import Dict
from abc import ABC, abstractmethod

class InterfaceOperadoraUseCase:

    @abstractmethod
    def import_operadoras(self, file_path: str) -> Dict: pass