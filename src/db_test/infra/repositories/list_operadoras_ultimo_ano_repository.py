from sqlalchemy import func, and_, or_
from sqlalchemy.sql.expression import cast
from sqlalchemy.types import Numeric
from datetime import datetime
from src.db_test.infra.settings.connection import DBConection
from src.db_test.infra.entities.demonstracoes_contabeis import DemonstracoesContabeis
from src.db_test.infra.entities.operadoras_ativas import Operadora
from src.db_test.data.interfaces.interface_list_operadoras_ultimo_ano_repository import InterfaceListOperadorasUltimoAnoRepository

class ListOperadorasUltimoAnoRepository(InterfaceListOperadorasUltimoAnoRepository):
    @classmethod
    def top_operadoras_ultimo_ano(cls):
        with DBConection() as db:
            today = datetime.now()
            start_date = today.replace(year=today.year-1, month=1, day=1)
            end_date = today.replace(month=1, day=1)
            
            despesas = DemonstracoesContabeis.vl_saldo_final - DemonstracoesContabeis.vl_saldo_inicial
            
            total_despesas_geral = db.session.query(
                func.sum(despesas)
            ).filter(
                and_(
                    DemonstracoesContabeis.data >= start_date,
                    DemonstracoesContabeis.data < end_date,
                    func.regexp_replace(DemonstracoesContabeis.descricao, '\\s+', ' ', 'g').ilike(
                        'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
                    )
                )
            ).scalar() or 1
            
            query = db.session.query(
                Operadora.razao_social.label('operadora'),
                Operadora.registro_ans,
                func.sum(despesas).label('total_despesas'),
                func.count(DemonstracoesContabeis.id).label('quantidade_registros'),
                (func.sum(despesas) / total_despesas_geral * 100).label('percentual_total')
            ).join(
                DemonstracoesContabeis,
                DemonstracoesContabeis.reg_ans == Operadora.registro_ans
            ).filter(
                and_(
                    DemonstracoesContabeis.data >= start_date,
                    DemonstracoesContabeis.data < end_date,
                    func.regexp_replace(DemonstracoesContabeis.descricao, '\\s+', ' ', 'g').ilike(
                        'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
                    )
                )
            ).group_by(
                Operadora.razao_social,
                Operadora.registro_ans
            ).order_by(
                func.sum(despesas).desc()
            ).limit(10)
            
            return query.all()