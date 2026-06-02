import time
import json
import os
from datetime import datetime
from system_scanner import run_scan

def run_scheduled_scan():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Running scan...")
    
    # Run the scan
    data = run_scan()
    
    # Add timestamp
    data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Save to history folder
    os.makedirs("output/history", exist_ok=True)
    filename = f"output/history/scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Scan saved to {filename}")

if __name__ == "__main__":
    print("🛡️ AI Security Assistant - Auto Scanner Started")
    print("Running a scan every hour. Press CTRL+C to stop.\n")
    
    while True:
        run_scheduled_scan()
        print("Next scan in 1 hour...\n")
        time.sleep(3600)
