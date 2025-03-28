from src.data_transformation.infra.repositories.extract_tables_repository import PdfTableExtractor
from src.data_transformation.infra.drivers.pandas_driver import PandasDriver
from src.data_transformation.data.use_cases.extract_tables_use_case import ExtractTablesUseCase

class CLIController:
    def run(self, pdf_path: str, csv_path: str):
        try:
            extractor = PdfTableExtractor()
            use_case = ExtractTablesUseCase(extractor, default_value="SEM VALOR")
            
            # Extrai e formata os dados
            data = use_case.extract_tables(pdf_path)
            
            # Salva o CSV formatado
            csv_path = PandasDriver().save_to_csv(data, csv_path)
            print(f"{len(data)} registros formatados e salvos em {csv_path}")
            
        except Exception as e:
            print(f"Falha: {str(e)}")
            raise