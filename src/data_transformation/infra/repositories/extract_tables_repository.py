from typing import List, Dict

from src.data_transformation.infra.drivers.pdfplumber_driver import PDFPlumberDriver
from src.data_transformation.infra.drivers.pandas_driver import PandasDriver
from src.data_transformation.data.interfaces.interface_extract_tables_repository import InterfacePdfRepository

class ExtractTablesRepository(InterfacePdfRepository):
    def __init__(self):
        self.pdf_driver = PDFPlumberDriver()
        self.csv_driver = PandasDriver()

    def extract(self, pdf_path: str) -> List[Dict]:
        """Extrai a tabela e converte os dados em um formato estruturado."""
        table_data = self.pdf_driver.extract_table(pdf_path)
        
        if not table_data:
            raise ValueError("Nenhuma tabela encontrada no PDF")
        
        # Assumindo que a primeira linha contém os cabeçalhos
        headers = table_data[0]
        rows = table_data[1:]
        
        return [dict(zip(headers, row)) for row in rows]
    
    def save_to_csv(self, data: List[Dict], output_path: str) -> str:
        """Salva os dados processados em CSV"""
        return self.csv_driver.save_to_csv(data, output_path)