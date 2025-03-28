from src.data_transformation.infra.drivers.pdfplumber_driver import PDFPlumberDriver
from src.data_transformation.data.interfaces.interface_extract_tables_repository import InterfacePdfRepository
from typing import List

class PdfTableExtractor(InterfacePdfRepository):
    def __init__(self):
        self.driver = PDFPlumberDriver()

    def extract(self, pdf_path: str) -> List[dict]:
        """Extrai a tabela e converte os dados em um formato estruturado."""
        table_data = self.driver.extract_table(pdf_path)
        
        if not table_data:
            raise ValueError("Nenhuma tabela encontrada no PDF")
        
        # Assumindo que a primeira linha contém os cabeçalhos
        headers = table_data[0]
        rows = table_data[1:]
        
        return [dict(zip(headers, row)) for row in rows]