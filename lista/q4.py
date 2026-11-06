from pathlib import Path

path = Path("lista/documentos/alunos.txt")

linhas = len(path.read_text().splitlines())

print(f"o numero de linhas é {linhas}")