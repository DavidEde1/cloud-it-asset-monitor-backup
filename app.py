
from flask import Flask, render_template_string
import platform
import psutil
from datetime import datetime

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Cloud IT Asset Monitor</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f1f5f9;
            margin: 0;
            padding: 30px;
            color: #1e293b;
        }
        h1 { color: #0f172a; }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
        }
        .card {
            background: white;
            padding: 24px;
            border-radius: 12px;
            box-shadow: 0 2px 8px #0001;
        }
        .value {
            font-size: 25px;
            font-weight: bold;
            color: #2563eb;
        }
        .status { color: #15803d; font-weight: bold; }
        .footer-line {
            border: 0;
            border-top: 1px solid #cbd5e1;
            width: 100%;
            max-width: 1200px;
            margin: 30px auto 16px;
        }
        .footer-note-wrap {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            max-width: 1200px;
            margin: 0 auto;
        }
        .footer-note-img {
            width: 22px;
            height: 22px;
            object-fit: cover;
            border-radius: 6px;
            display: block;
            margin-left: -32px;
        }
        .footer-note {
            text-align: center;
            font-style: italic;
            color: #475569;
            margin: 0;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <h1>Cloud IT Asset Monitoring Dashboard</h1>
    <p>Basic computer monitoring prototype</p>

    <div class="grid">
        <div class="card">
            <h3>Computer</h3>
            <p class="value">{{ computer }}</p>
        </div>
        <div class="card">
            <h3>Operating System</h3>
            <p class="value">{{ system }}</p>
        </div>
        <div class="card">
            <h3>CPU Usage</h3>
            <p class="value">{{ cpu }}%</p>
        </div>
        <div class="card">
            <h3>Memory Usage</h3>
            <p class="value">{{ memory }}%</p>
        </div>
        <div class="card">
            <h3>Disk Usage</h3>
            <p class="value">{{ disk }}%</p>
        </div>
        <div class="card">
            <h3>Monitoring Status</h3>
            <p class="status">ACTIVE</p>
            <p>Updated: {{ updated }}</p>
        </div>
    </div>

    <hr class="footer-line">
    <div class="footer-note-wrap">
        <img class="footer-note-img" src="EDE.png" alt="David Footer icon">
        <p class="footer-note"> ...Created by David Ede Ighoteguonor (a Computer Engineering Student FUPRE)</p>
    </div>
</body>
</html>
"""

@app.route("/")
def dashboard():
    return render_template_string(
        HTML,
        computer=platform.node(),
        system=f"{platform.system()} {platform.release()}",
        cpu=psutil.cpu_percent(interval=1),
        memory=psutil.virtual_memory().percent,
        disk=psutil.disk_usage("C:\\").percent,
        updated=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

if __name__ == "__main__":
    app.run(debug=True)