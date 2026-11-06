from pathlib import Path
import shutil
import os

# criar pastas
os.mkdir("imagens")


path = Path("documentos")

for arquivo in path.iterdir():
    if arquivo.suffix == ".bmp":
        shutil.move(f'documentos/{arquivo.name}',"imagens")
