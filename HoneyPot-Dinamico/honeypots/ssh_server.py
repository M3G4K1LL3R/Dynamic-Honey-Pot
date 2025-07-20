import socket
import logging
from datetime import datetime
import os

LOG_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs', 'honeypot.log')

os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(message)s')

HOST = '0.0.0.0'
PORT = 2222  # Porta falsa SSH

def registar_log(addr, data):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"{timestamp} | SSH | IP: {addr[0]} | Porta: {addr[1]} | Dados: {data.decode(errors='ignore')}"
    print(log_entry)
    logging.info(log_entry)

def start_honeypot():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[+] HoneyPot SSH ativo na porta {PORT}")

        while True:
            conn, addr = s.accept()
            with conn:
                data = conn.recv(1024)
                if data:
                    registar_log(addr, data)
                    conn.sendall(b"SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.3\r\n")

if __name__ == "__main__":
    start_honeypot()