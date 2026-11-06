from pathlib import Path

arquivo = input("Digite o nome do arquivo:  ")

path = Path(arquivo)  # Cria objeto pathlab

if path.is_file():
    print(f'P arquivo {arquivo} existe')
else:
    print(f'O arquivo {arquivo} não existe')
