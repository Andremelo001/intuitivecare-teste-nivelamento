from sqlalchemy import Column, String, Date, Integer
from src.db_test.infra.settings.base import Base

class Operadora(Base):
    __tablename__ = "operadora"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    registro_ans = Column(String(20), unique=True, nullable=False)
    cnpj = Column(String(20), unique=True, nullable=False)
    razao_social = Column(String(255), nullable=False)
    nome_fantasia = Column(String(255))
    modalidade = Column(String(100))
    logradouro = Column(String(255))
    numero = Column(String(20))
    complemento = Column(String(100))
    bairro = Column(String(100))
    cidade = Column(String(100))
    uf = Column(String(2))
    cep = Column(String(10))
    ddd = Column(String(2))
    telefone = Column(String(20))
    fax = Column(String(20))
    endereco_eletronico = Column(String(255))
    representante = Column(String(255))
    cargo_representante = Column(String(100))
    regiao_comercializacao = Column(Integer)
    data_registro_ans = Column(Date)