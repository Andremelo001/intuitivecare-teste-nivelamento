from sqlalchemy import func, and_, or_
from sqlalchemy.sql.expression import cast
from datetime import timedelta
from src.db_test.infra.settings.connection import DBConection
from src.db_test.infra.entities.demonstracoes_contabeis import DemonstracoesContabeis
from src.db_test.infra.entities.operadoras_ativas import Operadora
from src.db_test.data.interfaces.interface_list_operadoras_ultimo_trimestre_repository import InterfaceListOperadoraUltimoTrimestresRepository

class ListOperadorasUltimoTrimestreRepository(InterfaceListOperadoraUltimoTrimestresRepository):
    @classmethod
    def top_operadoras_ultimo_trimestre(cls):
        with DBConection() as db:
            # Obtém a data mais recente disponível no banco
            most_recent_date = db.session.query(
                func.max(DemonstracoesContabeis.data)
            ).scalar()
            
            if not most_recent_date:
                return []
            
            # Determina o primeiro dia do trimestre da data mais recente
            current_quarter = (most_recent_date.month - 1) // 3 + 1
            first_month_of_quarter = (current_quarter - 1) * 3 + 1
            first_day_of_quarter = most_recent_date.replace(month=first_month_of_quarter, day=1)
            
            # Define o início e fim do último trimestre completo
            start_date = first_day_of_quarter - timedelta(days=90)
            end_date = first_day_of_quarter
            
            # Calcula a diferença entre saldo final e inicial
            diferenca = DemonstracoesContabeis.vl_saldo_final - DemonstracoesContabeis.vl_saldo_inicial
            
            query = db.session.query(
                Operadora.razao_social.label('operadora'),
                Operadora.registro_ans,
                func.sum(diferenca).label('total_despesas'),
                func.count(DemonstracoesContabeis.id).label('quantidade_registros')
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
                func.sum(diferenca).desc()
            ).limit(10)
            
            return query.all()