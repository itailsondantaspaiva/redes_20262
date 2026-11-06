import conexao
import json

#Conectar-se ao equipamento RI do inventário.
with open('inventario.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

#'dados' agora é um dicionário ou lista Python

cliente=conexao.conectar(dados[0])

#Executar whoami , hostname e uptime -p .

codigo,saida,erro=conexao.executar(cliente, "whoami")

print(f"Código: {codigo}")
print(f"Saída: {saida}")
print(f"Erro: {erro}")

codigo,saida,erro=conexao.executar(cliente, "hostname")

print(f"Código: {codigo}")
print(f"Saída: {saida}")
print(f"Erro: {erro}")

codigo,saida,erro=conexao.executar(cliente, "uptime -p")

print(f"Código: {codigo}")
print(f"Saída: {saida}")
print(f"Erro: {erro}")

#Executar também um comando inexistente ( comando- inexistente ) e observar adiferença no código de saída.

codigo,saida,erro=conexao.executar(cliente, "comando- inexistente ")

print(f"Código: {codigo}")
print(f"Saída: {saida}")
print(f"Erro: {erro}")
