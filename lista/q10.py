from pathlib import Path

path = Path("documentos")

for arquivo in path.iterdir():
    if arquivo.is_file():
        if arquivo.suffix == ".txt," or arquivo.suffix == ".bmp": #definir qual extensão a ser usada
            print(arquivo.name)

