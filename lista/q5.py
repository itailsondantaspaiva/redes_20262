from pathlib import Path

path = Path("lista/documentos/usuarios.txt")

nome = input("Digite o nome:  ")
idade = input("Digite a idade:  ")
cidade = input("Digite a cidade:  ")

conteudo = f"""
Nome: {nome}
Idade: {idade}
Cidade: {cidade}
"""

path.write_text(conteudo)