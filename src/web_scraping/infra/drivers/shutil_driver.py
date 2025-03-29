import shutil
from typing import Optional

class ShutilDriver():
    @staticmethod
    def compress_file(base_name: str, root_dir: str, format: str = 'zip') -> Optional[str]:
        """
        Compacta um diretório para um arquivo ZIP
        
        Args:
            output_path: Caminho de saída (sem extensão)
            folder_to_compress: Diretório a ser compactado
            format: Formato de compressão ('zip', 'tar', etc.)
            
        Returns:
            Caminho completo do arquivo criado ou None em caso de falha
        """
        try:
            return shutil.make_archive(base_name=base_name, format=format, root_dir=root_dir)
        
        except Exception as e:
            print(f"Erro ao compactar: {str(e)}")
            return None