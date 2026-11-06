nome= 'Intelbras'
porta=22

echo "Dispositivo $nome, porta $porta"

#read -p "Digite seu IP:" ip
read -p "Você confirma?  $ip (Y/n)" resposta

echo $resposta

if [ "$resposta" == "" ]; then
    resposta="Y"
fi

echo "resposta: $resposta"