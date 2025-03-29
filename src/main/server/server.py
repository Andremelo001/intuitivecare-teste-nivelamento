from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.main.routes import web_scraping, data_transformation


# Configurações de inicialização do banco 
@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


# Inicializa o aplicativo FastAPI
app = FastAPI(lifespan=lifespan)

# Rotas para Endpoints
app.include_router(web_scraping.router)
app.include_router(data_transformation.router)
