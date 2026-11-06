import shutil

try: #comando para execução mesmo que houver erro na linha de comando
    shutil.move("foto.jpg", "imagens")
except FileNotFoundError:
    print("Aequivo não encontrado.")

print("Finalizado!!!")