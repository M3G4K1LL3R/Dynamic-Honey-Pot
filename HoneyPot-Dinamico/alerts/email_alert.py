
def send_alert(subject, body, to_email):
    print(f"Simulação de envio de alerta:\nAssunto: {subject}\nMensagem: {body}\nPara: {to_email}")

# Exemplo de uso
if __name__ == "__main__":
    send_alert("Alerta HoneyPot", "Tentativa de acesso detetada.", "destino@exemplo.com")
