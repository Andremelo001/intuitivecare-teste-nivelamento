from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.main.routes import web_scraping, data_transformation, db_test
from src.db_test.infra.settings.connection import init_db


# Configurações de inicialização do banco 
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


# Inicializa o aplicativo FastAPI
app = FastAPI(lifespan=lifespan)

# Rotas para Endpoints
app.include_router(web_scraping.router)
app.include_router(data_transformation.router)
app.include_router(db_test.router)
