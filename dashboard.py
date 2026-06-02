from flask import Flask, render_template_string
import json

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Security Assistant</title>
    <style>
        body { font-family: Arial, sans-serif; background: #0d1117; color: #c9d1d9; padding: 20px; }
        h1 { color: #58a6ff; }
        .card { background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 20px; margin: 10px 0; }
        .clean { color: #3fb950; }
        .risk { color: #f85149; }
        .label { color: #8b949e; font-size: 0.85em; }
        .value { font-size: 1.1em; font-weight: bold; }
        .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }
    </style>
</head>
<body>
    <h1>🛡️ AI Security Assistant</h1>
    <div class="card">
        <h2>💻 System</h2>
        <p><span class="label">OS:</span> <span class="value">{{ data['system']['os'] }}</span></p>
        <p><span class="label">Version:</span> <span class="value">{{ data['system']['os_version'] }}</span></p>
        <p><span class="label">Machine:</span> <span class="value">{{ data['system']['machine'] }}</span></p>
    </div>
    <div class="card">
        <h2>🌐 Network</h2>
        <p><span class="label">Hostname:</span> <span class="value">{{ data['network']['hostname'] }}</span></p>
        <p><span class="label">IP Address:</span> <span class="value">{{ data['network']['ip_address'] }}</span></p>
    </div>
    <div class="card">
        <h2>⚡ CPU & Memory</h2>
        <div class="grid">
            <div><span class="label">CPU Usage</span><br><span class="value">{{ data['cpu_memory']['cpu_percent'] }}%</span></div>
            <div><span class="label">CPU Cores</span><br><span class="value">{{ data['cpu_memory']['cpu_cores'] }}</span></div>
            <div><span class="label">Memory Used</span><br><span class="value">{{ data['cpu_memory']['memory_percent'] }}%</span></div>
            <div><span class="label">Total RAM</span><br><span class="value">{{ data['cpu_memory']['memory_total_gb'] }} GB</span></div>
            <div><span class="label">Used RAM</span><br><span class="value">{{ data['cpu_memory']['memory_used_gb'] }} GB</span></div>
        </div>
    </div>
    <div class="card">
        <h2>🔓 Open Ports</h2>
        {% for port in data['open_ports'] %}
        <p>Port <span class="value">{{ port['port'] }}</span> — {{ port['address'] }} ({{ port['status'] }})</p>
        {% endfor %}
    </div>
    <div class="card">
        <h2>🚨 Security Risks</h2>
        {% for risk in data['risks'] %}
        <p class="{{ 'clean' if risk['type'] == 'clean' else 'risk' }}">{{ risk['detail'] }}</p>
        {% endfor %}
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    with open("output/report.json") as f:
        data = json.load(f)
    return render_template_string(HTML, data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
