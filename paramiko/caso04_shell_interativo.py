import json
import os
import time
from conexao import conectar, executar

# Carrega R1 do seu inventario.json
with open("inventario.json", encoding="utf-8") as f:
    dispositivo = json.load(f)[0]

if dispositivo.get("chave"):
    dispositivo["chave"] = os.path.expanduser(dispositivo["chave"])


def ler(canal, pausa=0.6):
    """Aguarda e lê tudo o que o equipamento enviou."""
    time.sleep(pausa)
    dados = ""
    while canal.recv_ready():
        dados += canal.recv(65535).decode(errors="ignore")
        time.sleep(0.1)
    return dados


sequencia = ["cd /tmp", "pwd", "export AMBIENTE=PRODUCAO", "echo $AMBIENTE"]

cliente = conectar(dispositivo)
try:
    print("=== SESSAO INTERATIVA (invoke_shell) ===")
    canal = cliente.invoke_shell()
    ler(canal)  # descarta o banner inicial
    for cmd in sequencia:
        canal.send(cmd + "\n")
        print(ler(canal))
    canal.close()

    print("=== UM COMANDO POR CHAMADA (exec_command) ===")
    for cmd in sequencia:
        _, saida, _ = executar(cliente, cmd)
        print(f"$ {cmd} -> {saida!r}")
finally:
    cliente.close()