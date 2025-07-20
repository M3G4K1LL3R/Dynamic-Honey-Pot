
import subprocess

# Comandos para iniciar cada honeypot
honeypots = [
    "python honeypots/ssh_server.py",
    "python honeypots/ftp_server.py",
    "python honeypots/http_server.py"
]

processos = []

try:
    for comando in honeypots:
        print(f"[+] A iniciar: {comando}")
        proc = subprocess.Popen(comando, shell=True)
        processos.append(proc)

    print("[+] Todos os honeypots estão ativos. Ctrl+C para parar.")

    for proc in processos:
        proc.wait()

except KeyboardInterrupt:
    print("\n[!] Interrompido pelo utilizador. A terminar honeypots...")
    for proc in processos:
        proc.terminate()
