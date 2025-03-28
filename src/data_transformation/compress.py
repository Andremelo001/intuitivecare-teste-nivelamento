from src.web_scraping.presentation.controllers.controller_compress import ControllerCompress

if __name__ == "__main__":
    ControllerCompress().run(
        diretorio_destino = "data/processed",
        name_zip = "Teste_AndréMelo",
        diretorio_origem = "data/csv"
    )