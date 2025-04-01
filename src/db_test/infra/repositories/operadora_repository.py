import csv
from typing import Dict
from datetime import datetime
from typing import Optional
from src.db_test.infra.settings.connection import DBConection
from src.db_test.infra.entities.operadoras_ativas import Operadora

class OperadoraRepository:
    def __init__(self):
        self.db = DBConection()

    def _parse_regiao_comercializacao(self, value: str) -> Optional[int]:
        """Converte Regiao_de_Comercializacao para int ou retorna None se vazio"""
        cleaned = value.strip('"').strip()
        return int(cleaned) if cleaned else None

    def _parse_telefone(self, value: str) -> str:
        """Remove caracteres não numéricos de telefones"""
        return ''.join(filter(str.isdigit, value.strip('"'))) if value else None

    def import_operadoras_csv(self, file_path: str) -> Dict:
        """
        Importa arquivo CSV de operadoras com tratamento robusto de erros
        Retorna: {
            'total_lines': int,
            'imported': int,
            'errors': int,
            'details': list
        }
        """
        result = {
            'total_lines': 0,
            'imported': 0,
            'errors': 0,
            'details': []
        }
        
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            result['total_lines'] = sum(1 for _ in reader)  # Conta total de linhas
            file.seek(0)  # Volta ao início do arquivo
            next(reader)  # Pula cabeçalho
            
            with self.db as db:
                batch = []
                batch_size = 500  # Reduzido para melhor debug
                
                for row in reader:
                    try:
                        operadora = {
                            'registro_ans': row['Registro_ANS'].strip('"'),
                            'cnpj': row['CNPJ'].strip('"'),
                            'razao_social': row['Razao_Social'].strip('"'),
                            'nome_fantasia': row['Nome_Fantasia'].strip('"') or None,
                            'modalidade': row['Modalidade'].strip('"'),
                            'logradouro': row['Logradouro'].strip('"'),
                            'numero': row['Numero'].replace('"', '').split('.')[0],  # Trata "95.0"
                            'complemento': row['Complemento'].strip('"') or None,
                            'bairro': row['Bairro'].strip('"'),
                            'cidade': row['Cidade'].strip('"'),
                            'uf': row['UF'].strip('"'),
                            'cep': row['CEP'].strip('"'),
                            'ddd': row['DDD'].strip('"'),
                            'telefone': self._parse_telefone(row['Telefone']),
                            'fax': self._parse_telefone(row['Fax']) if row['Fax'].strip('"') else None,
                            'endereco_eletronico': row['Endereco_eletronico'].strip('"').lower() or None,
                            'representante': row['Representante'].strip('"'),
                            'cargo_representante': row['Cargo_Representante'].strip('"'),
                            'regiao_comercializacao': self._parse_regiao_comercializacao(row['Regiao_de_Comercializacao']),
                            'data_registro_ans': datetime.strptime(row['Data_Registro_ANS'].strip('"'), '%Y-%m-%d').date()
                        }
                        batch.append(operadora)
                        
                        if len(batch) >= batch_size:
                            db.session.bulk_insert_mappings(Operadora, batch)
                            db.session.commit()
                            result['imported'] += len(batch)
                            batch = []
                            
                    except Exception as e:
                        result['errors'] += 1
                        result['details'].append({
                            'line': reader.line_num,
                            'error': str(e),
                            'data': row
                        })                
                if batch:
                    try:
                        db.session.bulk_insert_mappings(Operadora, batch)
                        db.session.commit()
                        result['imported'] += len(batch)
                    except Exception as e:
                        result['errors'] += len(batch)
                        result['details'].append({
                            'line': 'batch_final',
                            'error': str(e),
                            'data': f"Erro no batch final com {len(batch)} registros"
                        })
        
        return result