from abc import ABC, abstractmethod
from typing import Dict

class InterfaceDataImporterUseCase(ABC):
    @abstractmethod
    def process_csv(self, directory_path: str) -> Dict: pass