
from flask import Flask, render_template, request
import os

app = Flask(__name__)

LOG_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs', 'honeypot.log')

@app.route("/")
def dashboard():
    service_filter = request.args.get('service')
    logs = []
    counts = {'SSH': 0, 'FTP': 0, 'HTTP': 0}

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            for line in f:
                logs.append(line.strip())
                for service in counts:
                    if f"| {service} |" in line:
                        counts[service] += 1

    if service_filter and service_filter in counts:
        logs = [log for log in logs if f"| {service_filter} |" in log]

    total_logs = sum(counts.values())
    return render_template("dashboard.html", logs=logs, counts=counts, total=total_logs, filter=service_filter)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
