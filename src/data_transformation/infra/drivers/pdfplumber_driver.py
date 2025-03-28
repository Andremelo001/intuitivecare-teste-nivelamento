import pdfplumber
from typing import List
import logging

class PDFPlumberDriver:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def extract_table(self, pdf_path: str) -> List[List[str]]:
        """Extrai tabelas do PDF e retorna uma lista de listas (linhas e colunas)."""
        tables = []
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    table = page.extract_table()
                    if table:
                        tables.extend(table)
            return tables
        except Exception as e:
            self.logger.error(f"Falha ao extrair tabela: {str(e)}")
            raise