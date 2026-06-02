# 🛡️ AI Security Assistant

An AI-powered endpoint security auditing and analysis system built in Python.

## Features
- 💻 System info (OS, machine, processor)
- 🌐 Network info (hostname, IP address)
- ⚡ CPU & memory monitoring
- 🔓 Open ports detection
- 🚨 Security risk flagging
- 📊 Web dashboard
- 🕐 Automatic hourly scans with history logging

## How to Run

### Run a single scan
```bash
python main.py
```

### Launch the web dashboard
```bash
python dashboard.py
```
Then open http://localhost:5000

### Start automatic hourly scanning
```bash
python scheduler.py
```

## Output
- Latest scan saved to `output/report.json`
- Scan history saved to `output/history/`

## Tech Stack
- Python 3
- Flask (web dashboard)
- psutil (system monitoring)
