from pathlib import Path

path = Path("lista/documentos/acessos.txt")

conteudo =path.read_text()
linhas = conteudo.splitlines()

numero_sucessos = 0
numero_erros = 0

for linha in linhas:
    if linha == "sucesso":
        numero_sucessos = numero_sucessos + 1
    if linha == "erro":
            numero_erros = numero_erros + 1
            
print(f"Número de sucessos: {numero_sucessos}")
print(f"Número de erros: {numero_erros}")