
# Projeto HoneyPot Dinâmico

Este projeto implementa um sistema de HoneyPot com serviços falsos (**SSH, FTP, HTTP**), um painel web em **Flask** para visualização dos logs, sistema de alertas simulados e assinatura digital dos logs.

---

## ✅ Requisitos
- Python 3.x
- pip install flask cryptography

---

## 📂 Estrutura de Pastas
- `honeypots/`: contém `ssh_server.py`, `ftp_server.py`, `http_server.py`
- `webpanel/`: contém o painel Flask (`app.py`) e o template HTML
- `alerts/`: alerta de e-mail (simulado)
- `crypto/`: assinatura digital dos logs
- `logs/`: logs gerados pelos honeypots

---

## 🚀 Como Usar

1. **Iniciar todos os honeypots de uma vez:**
```
python start_all.py
```

2. **Ver os logs pelo Dashboard web:**
```
cd webpanel
python app.py
```
Aceder em:  
[http://localhost:5000](http://localhost:5000)

3. **Assinar digitalmente o ficheiro de logs:**
```
python crypto/crypto_utils.py
```

4. **Simular envio de alerta por e-mail:**
```
python alerts/email_alert.py
```

---

## 🧪 Testes dos Honeypots

- SSH:  
```
telnet localhost 2222
```

- FTP:  
```
telnet localhost 2121
```

- HTTP:  
```
curl http://localhost:8080
```

Verificar as atualizações no **Dashboard web**.

---

## ⛔ Parar os serviços
Ctrl+C no terminal onde está a correr o `start_all.py` ou cada honeypot individualmente.

---

## 🔒 Licença
MIT License - veja o ficheiro LICENSE para mais informações.
