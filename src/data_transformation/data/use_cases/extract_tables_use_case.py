from pathlib import Path
from typing import List, Dict, Optional
from src.data_transformation.data.interfaces.interface_extract_tables_repository import InterfacePdfRepository
from src.data_transformation.domain.interfaces.interface_extract_tables_use_case import InterfaceExtractTablesUseCase

class ExtractTablesUseCase(InterfaceExtractTablesUseCase):
    def __init__(self, repository: InterfacePdfRepository, default_value: str = "N/A"):
        """
        Args:
            repository: Repositório para extração e conversão de tabelas
            default_value: Valor padrão para substituir nulos/vazios (default: "N/A")
        """
        self.repository = repository
        self.default_value = default_value
        self.abbreviation_map = {
            "OD": "Seg. Odontológica",
            "AMB": "Seg. Ambulatorial"
        }

    def extract_tables(self, pdf_path: str, output_path: str) -> str:
        """
        Extrai tabelas do PDF, aplica transformações e salva em CSV
        
        Args:
            pdf_path: Caminho do arquivo PDF de entrada
            output_path: Caminho para o arquivo CSV de saída
            
        Returns:
            Caminho completo do arquivo CSV gerado
        """
        try:
            self._diretorio_exists(output_path)

            status_file = self._verificar_arquivos(output_path)

            if status_file['procedimentos']['status'] == 'presente':
                return {"message": "Arquivo já presente no diretório"}

            # Extrai dados brutos do PDF
            raw_data = self.repository.extract(pdf_path)  # Arquivo temporário
            
            # Processa e formata os dados
            processed_data = self._process_raw_data(raw_data)
            
            # Salva os dados processados
            return self.repository.save_to_csv(processed_data, output_path)
            
        except Exception as e:
            raise RuntimeError(f"Falha ao processar PDF: {str(e)}")

    def _process_raw_data(self, raw_data: List[Dict]) -> List[Dict]:
        """Aplica todas as transformações nos dados brutos"""
        processed_data = []
        
        for row in raw_data:
            processed_row = {}
            for key, value in row.items():
                formatted_key = self._format_header(key)
                formatted_value = self._format_value(value)
                formatted_value = self._replace_abbreviations(formatted_key, formatted_value)
                
                processed_row[formatted_key] = formatted_value
            
            processed_data.append(processed_row)
        
        return processed_data

    def _replace_abbreviations(self, column_name: str, value: str) -> str:
        """Substitui abreviações conforme mapeamento"""
        if column_name in self.abbreviation_map:
            if value in self.abbreviation_map:
                return self.abbreviation_map[value]
            if "," in value:
                parts = [part.strip() for part in value.split(",")]
                return ", ".join(self.abbreviation_map.get(part, part) for part in parts)
        return value

    @classmethod
    def _format_header(cls, header: str) -> str:
        """Padroniza nomes de colunas"""
        if not header:
            return "COLUNA_DESCONHECIDA"
            
        return (header
                .replace('\n', ' ')
                .replace('"', '')
                .upper()
                .translate(str.maketrans('ÍÃÇ', 'IAC'))
                .replace(',', ';'))

    def _format_value(self, value: Optional[str]) -> str:
        """Padroniza valores das células"""
        if not value or not str(value).strip():
            return self.default_value
            
        return ' '.join(str(value)
                        .replace('\n', ' ')
                        .replace('"', '')
                        .split())
    
    @classmethod
    def _diretorio_exists(cls, output_path: str) -> None:
        """Verifica se o diretório existe e cria se necessário"""
        Path(output_path).mkdir(parents=True, exist_ok=True)

    @classmethod
    def _verificar_arquivos(cls, output_path: str) -> Dict:
        """Verifica se os arquivos já existem no diretório"""
        arquivos = {
            'procedimentos': Path(output_path) / "procedimentos.csv",
        }

        arquivos_encontrados = {
            chave: {
                'status': 'presente' if arquivo.exists() else 'ausente',
                'caminho': str(arquivo.resolve()),
            }
            for chave, arquivo in arquivos.items()
        }

        return arquivos_encontrados