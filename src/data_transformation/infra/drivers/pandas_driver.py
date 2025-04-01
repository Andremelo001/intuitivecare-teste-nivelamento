import pandas as pd
from typing import List
import logging
import os
from pathlib import Path

class PandasDriver:
    def save_to_csv(self, data: List[dict], output_path: str) -> str:
        try:                                
            # Verificar se é um arquivo, não diretório
            if os.path.isdir(output_path):
                raise ValueError(f"O caminho {output_path} é um diretório, não um arquivo")
                
            df = pd.DataFrame(data)
            df.to_csv(output_path, index=False, encoding='utf-8-sig')
            return output_path
            
        except Exception as e:
            logging.error(f"Erro ao salvar CSV: {str(e)}")
            raise