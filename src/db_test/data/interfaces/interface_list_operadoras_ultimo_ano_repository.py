from abc import ABC, abstractmethod

class InterfaceListOperadorasUltimoAnoRepository(ABC):

    @abstractmethod
    def top_operadoras_ultimo_ano(self): pass