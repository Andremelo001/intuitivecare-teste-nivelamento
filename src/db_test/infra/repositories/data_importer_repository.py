import csv
import os
from decimal import Decimal
from datetime import datetime, date
from typing import Tuple, List, Dict
from src.db_test.infra.settings.connection import DBConection
from src.db_test.infra.entities.demonstracoes_contabeis import DemonstracoesContabeis
from src.db_test.data.interfaces.interface_data_importer_repository import InterfaceDateImporterRepository

class DataImporterRepository(InterfaceDateImporterRepository):
    def __init__(self):
        self.db = DBConection()

    @classmethod
    def _convert_decimal(cls, value: str) -> Decimal:
        """Converte string para Decimal, tratando valores vazios e formatos inválidos"""
        try:
            cleaned = value.replace('.', '').replace(',', '.').strip()
            return Decimal(cleaned) if cleaned else Decimal('0')
        except:
            return Decimal('0')
        
    @classmethod
    def _parse_date(cls, date_str: str) -> date:
        """Tenta converter uma string de data em vários formatos para um objeto date
        
        Args:
            date_str: String contendo a data em algum formato
            
        Returns:
            Objeto date correspondente
            
        Raises:
            ValueError: Se nenhum dos formatos conhecidos corresponder
        """
        for fmt in ('%d/%m/%Y', '%Y-%m-%d', '%m/%d/%Y'):
            try:
                return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        raise ValueError(f"Formato de data não reconhecido: '{date_str}'")

    def _process_csv_file(self, file_path: str) -> Tuple[List[dict], int]:
        """Processa um único arquivo CSV e retorna (registros válidos, erros)"""
        records = []
        errors = 0
        
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            
            for row in reader:
                try:
                    if not any(row.values()):
                        continue
                        
                    record = {
                        'data': self._parse_date(row['DATA']),
                        'reg_ans': row['REG_ANS'].strip(),
                        'cd_conta_contabil': row['CD_CONTA_CONTABIL'].strip(),
                        'descricao': row['DESCRICAO'].strip(),
                        'vl_saldo_inicial': self._convert_decimal(row['VL_SALDO_INICIAL']),
                        'vl_saldo_final': self._convert_decimal(row['VL_SALDO_FINAL'])
                    }
                    records.append(record)
                except ValueError as e:
                    errors += 1
                    print(f"Erro de formato no arquivo {os.path.basename(file_path)}, linha {reader.line_num}: {str(e)}")
                except Exception as e:
                    errors += 1
                    print(f"Erro inesperado no arquivo {os.path.basename(file_path)}, linha {reader.line_num}: {str(e)}")
        
        return records, errors

    def process_csv_directory(self, directory_path: str) -> Dict:
        """
        Importa todos os arquivos CSV de um diretório
        Retorna: {
            'total_files': int,
            'imported': int,
            'errors': int,
            'file_details': List[dict]
        }
        """
        results = {
            'total_files': 0,
            'imported': 0,
            'errors': 0,
            'file_details': []
        }
        
        # Lista todos os arquivos CSV no diretório
        csv_files = [f for f in os.listdir(directory_path) 
                    if f.lower().endswith('.csv')]
        
        results['total_files'] = len(csv_files)
        
        with self.db as db:
            for csv_file in csv_files:
                file_path = os.path.join(directory_path, csv_file)
                file_stats = {
                    'filename': csv_file,
                    'imported': 0,
                    'errors': 0
                }
                
                try:
                    # Processa o arquivo CSV
                    records, file_errors = self._process_csv_file(file_path)
                    file_stats['errors'] = file_errors
                    
                    if records:
                        # Insere em lotes para melhor performance
                        batch_size = 1000
                        for i in range(0, len(records), batch_size):
                            batch = records[i:i + batch_size]
                            db.session.bulk_insert_mappings(DemonstracoesContabeis, batch)
                            db.session.commit()
                            file_stats['imported'] += len(batch)
                            results['imported'] += len(batch)
                    
                    results['errors'] += file_errors
                
                except Exception as e:
                    file_stats['errors'] += 1
                    results['errors'] += 1
                    print(f"Erro ao processar arquivo {csv_file}: {str(e)}")
                
                results['file_details'].append(file_stats)
        
        return results