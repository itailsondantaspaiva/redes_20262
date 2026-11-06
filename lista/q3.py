from pathlib import Path

path = Path("lista/documentos/nomes.txt")

conteudo = path.read_text()

print(conteudo)