# Dynamic HoneyPot Project

This project implements a **dynamic HoneyPot system** in Python that emulates fake services (**SSH, FTP, HTTP**), providing real-time logging, a Flask-based web dashboard, simulated alerting, and digital signing of the logs.

---

## ✅ Requirements
- Python 3.x
- Install dependencies:
```
pip install flask cryptography
```

---

## 📂 Project Structure
- `honeypots/`: Contains `ssh_server.py`, `ftp_server.py`, `http_server.py`
- `webpanel/`: Flask dashboard (`app.py`) and the HTML template
- `alerts/`: Simulated email alert
- `crypto/`: Digital signature for the logs
- `logs/`: Generated logs by the honeypots

---

## 🚀 How to Use

1. **Start all honeypots at once:**
```
python start_all.py
```

2. **View logs on the web dashboard:**
```
cd webpanel
python app.py
```
Access at:  
[http://localhost:5000](http://localhost:5000)

3. **Digitally sign the log file:**
```
cd crypto
python crypto_utils.py
```

4. **Simulate sending an email alert:**
```
python alerts/email_alert.py
```

---

## 🧪 Testing the Honeypots

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

Check the updates on the **web dashboard**.

---

## ⛔ Stop Services
Press **Ctrl+C** on the terminal where `start_all.py` or each honeypot is running.

---

## 🔒 License
MIT License - see the LICENSE file for more details.
