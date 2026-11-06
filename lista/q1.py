"""
O operador / permite concatenar paths, isso ajuda definir caminhos, isso ajuda a definir caminhos para explorar pastas e arquivos

IMPORTANTE? ele tem esse uso apenas quando utilizado junto a pathlib
"""

from pathlib import Path
arquivo = Path('documentos') / 'relatorio.txt'
print(arquivo)
print(arquivo.is_dir())   # Informa se é um diretório
print(arquivo.is_file())  # Informa se é um arquivo
print(arquivo.exists())   # Informa se é um path válido (arquivo ou dir)