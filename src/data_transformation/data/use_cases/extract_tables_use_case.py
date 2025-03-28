from typing import List, Dict, Optional
from src.data_transformation.data.interfaces.interface_extract_tables_repository import InterfacePdfRepository
from src.data_transformation.domain.interfaces.interface_extract_tables_use_case import InterfaceExtractTablesUseCase

class ExtractTablesUseCase(InterfaceExtractTablesUseCase):
    def __init__(self, repository: InterfacePdfRepository, default_value: str = "N/A"):
        """
        Args:
            repository: Repositório para extração de tabelas
            default_value: Valor padrão para substituir nulos/vazios (default: "N/A")
        """
        self.repository = repository
        self.default_value = default_value
        self.abbreviation_map = {
            "OD": "Seg. Odontológica",
            "AMB": "Seg. Ambulatorial"
        }

    def extract_tables(self, pdf_path: str) -> List[Dict]:
        raw_data = self.repository.extract(pdf_path)
        formatted_data = []
        
        for row in raw_data:
            formatted_row = {}
            for key, value in row.items():
                formatted_key = self.__format_header(key)
                formatted_value = self.__format_value(value)
                
                # Aplica substituição de abreviações para valores nas colunas específicas
                formatted_value = self.__replace_abbreviations(formatted_key, formatted_value)
                
                formatted_row[formatted_key] = formatted_value
            
            formatted_data.append(formatted_row)
        
        return formatted_data

    def __replace_abbreviations(self, column_name: str, value: str) -> str:
        """
        Substitui abreviações pelas descrições completas em colunas específicas.
        
        Args:
            column_name: Nome da coluna sendo processada
            value: Valor atual da célula
            
        Returns:
            Valor com abreviações substituídas quando aplicável
        """
        # Verifica se é uma coluna que pode conter abreviações
        if column_name in ["OD", "AMB"]:
            # Se o valor for exatamente a abreviação, substitui
            if value in self.abbreviation_map:
                return self.abbreviation_map[value]
            # Se for uma lista separada por vírgulas, processa cada item
            elif "," in value:
                parts = [part.strip() for part in value.split(",")]
                replaced = [self.abbreviation_map.get(part, part) for part in parts]
                return ", ".join(replaced)
        
        return value

    @classmethod
    def __format_header(cls, header: str) -> str:
        """Formata os cabeçalhos da tabela"""
        if header is None:
            return "COLUNA_DESCONHECIDA"
            
        formatted = header.replace('\n', ' ').strip()
        formatted = formatted.replace('"', '')
        formatted = ' '.join(formatted.split()).upper()
        formatted = formatted.replace('Í', 'I').replace('Ã', 'A').replace('Ç', 'C')
        formatted = formatted.replace(',', ';')
        return formatted

    def __format_value(self, value: Optional[str]) -> str:
        """Formata os valores das células da tabela"""
        # Verifica se o valor é nulo ou string vazia
        if value is None or (isinstance(value, str) and not value.strip()):
            return self.default_value
            
        # Remove quebras de linha e espaços extras
        formatted = str(value).replace('\n', ' ').strip()
        
        # Remove aspas duplas se existirem
        formatted = formatted.replace('"', '')
        
        # Remove espaços duplicados
        formatted = ' '.join(formatted.split())
        
        return formatted