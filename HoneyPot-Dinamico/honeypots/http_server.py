import socket
import logging
from datetime import datetime
import os

LOG_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs', 'honeypot.log')

os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(message)s')

HOST = '0.0.0.0'
PORT = 8080  # Porta HTTP falsa

def registar_log(addr, data):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"{timestamp} | HTTP | IP: {addr[0]} | Porta: {addr[1]} | Dados: {data.decode(errors='ignore')}"
    print(log_entry)
    logging.info(log_entry)

def start_honeypot():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[+] HoneyPot HTTP ativo na porta {PORT}")

        while True:
            conn, addr = s.accept()
            with conn:
                data = conn.recv(1024)
                if data:
                    registar_log(addr, data)
                    response = b"""HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html><body><h1>It works!</h1></body></html>\r\n"""
                    conn.sendall(response)

if __name__ == "__main__":
    start_honeypot()