#!/bin/bash
# diagnostico.sh - script de checagem de sistema
LOG="diagnostico_$(date +%Y%m%d).log"
echo "=== Diagnóstico em $(date) ===" >> "$LOG"
echo "--- Uso de disco ---" >> "$LOG"
df -h >> "$LOG"
echo "--- Processos ativos (top 5 por memória) ---" >> "$LOG"
ps aux --sort=-%mem | head -6 >> "$LOG"
echo "--- Tempo ativo ---" >> "$LOG"
uptime >> "$LOG"
echo "Diagnóstico salvo em $LOG"