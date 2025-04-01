from abc import ABC, abstractmethod
from typing import Dict

class InterfaceListOperadorasUltimoTrimestreUseCase(ABC):
    
    @abstractmethod
    def list_operadoras(self) -> Dict: pass