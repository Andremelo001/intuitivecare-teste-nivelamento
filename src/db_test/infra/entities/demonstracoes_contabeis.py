from sqlalchemy import Column, Date, String, Numeric, Integer
from src.db_test.infra.settings.base import Base

class DemonstracoesContabeis(Base):
    __tablename__ = "demonstracoescontabeis"

    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(Date, nullable=False)
    reg_ans = Column(String, nullable=False)
    cd_conta_contabil = Column(String, nullable=False)
    descricao = Column(String)
    vl_saldo_inicial = Column(Numeric(15, 2))
    vl_saldo_final = Column(Numeric(15, 2))