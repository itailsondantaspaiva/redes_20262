#!/bin/bash
# config_interface.sh - configura e valida uma interface de rede
IFACE="dummy0"
IP="10.10.10.2/24"
LOG="config_interface_$(date +%Y%m%d).log"
sudo ip link set "$IFACE" down
echo "=== Configuração em $(date) ===" > "$LOG"
echo "--- Status antes ---" >> "$LOG"
ip addr show "$IFACE" >> "$LOG" 2>> "$LOG"
sudo ip link set "$IFACE" up
sudo ip addr add "$IP" dev "$IFACE"
echo "--- Status depois ---" >> "$LOG"
ip addr show "$IFACE" >> "$LOG"

# Testa se a interface responde (ping local)
if ping -c 2 "$IP" > /dev/null 2>> "$LOG"; then
echo "Interface $IFACE respondendo normalmente" >> "$LOG"
else
echo "FALHA: $IFACE não respondeu ao ping" >> "$LOG"
fi
