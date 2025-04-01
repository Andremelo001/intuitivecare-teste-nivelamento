from src.db_test.infra.settings.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConection:
    def __init__(self):
        self.__connection_string = "postgresql://teste3:test3intuitivecare@localhost:5432/demonstracoes_contabeis"
        self.__engine = self.__create_database_engine()
        self.Session = sessionmaker(bind=self.__engine)  # Note: Session com S maiúsculo é a fábrica
        self.session = None  # Sessão atual

    def __create_database_engine(self):
        return create_engine(self.__connection_string)

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        self.session = self.Session()  # Cria uma nova sessão
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            self.session.close()

# Instância global
db = DBConection()

def init_db():
    """Cria todas as tabelas definidas nos modelos"""
    Base.metadata.create_all(db.get_engine())
    

