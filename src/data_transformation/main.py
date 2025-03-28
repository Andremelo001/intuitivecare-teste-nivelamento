from src.data_transformation.presentation.controllers.controller import CLIController

if __name__ == "__main__":
    CLIController().run(
        pdf_path="data/raw/Anexo_I.pdf",
        csv_path="data/csv/procedimentos.csv"
    )