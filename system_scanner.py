import platform
import socket
import json
import os

# Get system information
def get_system_info():
    return {
        "os": platform.system(),
        "os_version": platform.release(),
        "machine": platform.machine(),
        "processor": platform.processor()
    }

# Get network information
def get_network_info():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)

    return {
        "hostname": hostname,
        "ip_address": ip
    }

# Run full scan and save results
def run_scan():
    data = {
        "system": get_system_info(),
        "network": get_network_info(),
        "processes": get_running_processes()
    }

    # Ensure output folder exists
    os.makedirs("output", exist_ok=True)

    # Save to JSON file
    with open("output/report.json", "w") as f:
        json.dump(data, f, indent=4)

    return data


# Get running processes
def get_running_processes():
    import psutil
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'status']):
        try:
            processes.append(proc.info)
        except psutil.NoSuchProcess:
            pass
    return processes
