import csv
import json
from concurrent.futures import ThreadPoolExecutor
import conexao

# Colunas que farão parte do cabeçalho do arquivo CSV
COLUNAS = ["nome", "usuario", "hostname", "kernel", "uptime", "status"]


def coletar(disp):
    """Função responsável por conectar a UM dispositivo e coletar suas informações."""
    # Inicializa o dicionário com campos vazios
    registro = {c: "" for c in COLUNAS}
    registro["nome"] = disp["nome"]

    try:
        # Abre conexão no estilo do professor
        cliente = conexao.conectar(disp)
        try:
            # Executa os 4 comandos exigidos no requisito
            _, usuario, _ = conexao.executar(cliente, "whoami")
            _, hostname, _ = conexao.executar(cliente, "hostname")
            _, kernel, _ = conexao.executar(cliente, "uname -r")
            _, uptime, _ = conexao.executar(cliente, "uptime -p")

            # Armazena os resultados coletados
            registro["usuario"] = usuario
            registro["hostname"] = hostname
            registro["kernel"] = kernel
            registro["uptime"] = uptime
            registro["status"] = "OK"
        finally:
            # Garante que a conexão seja fechada mesmo se algum comando falhar
            cliente.close()

    except Exception as e:
        # Se houver erro de conexão/autenticação, registra a falha sem parar o script
        registro["status"] = f"FALHA: {type(e).__name__}"

    return registro


# --- EXECUÇÃO PRINCIPAL ---

# 1. Ler o inventario.json (mesmo raciocínio do Caso 1)
with open("inventario.json", "r", encoding="utf-8") as arquivo:
    inventario = json.load(arquivo)

# 2. Executar as coletas em paralelo usando ThreadPoolExecutor
# max_workers=10 permite até 10 conexões simultâneas
with ThreadPoolExecutor(max_workers=10) as pool:
    resultados = list(pool.map(coletar, inventario))

# 3. Gerar e salvar o arquivo inventario_coletado.csv
with open("inventario_coletado.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.DictWriter(f, fieldnames=COLUNAS)
    escritor.writeheader()
    escritor.writerows(resultados)

# 4. Exibir o resultado final formatado no terminal
print(f"{'NOME':<6} {'STATUS':<12} {'USUÁRIO':<8} {'UPTIME'}")
print("-" * 55)
for r in resultados:
    print(f"{r['nome']:<6} {r['status']:<12} {r['usuario']:<8} {r['uptime']}")