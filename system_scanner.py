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
        "processes": get_running_processes(),
        "open_ports": get_open_ports()
    }

    # Ensure output folder exists
    os.makedirs("output", exist_ok=True)

    # Save to JSON file
    with open("output/report.json", "w") as f:
        json.dump(data, f, indent=4)

    data["risks"] = get_security_risks(data)
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

# Get open ports
def get_open_ports():
    import psutil
    open_ports = []
    for conn in psutil.net_connections(kind='inet'):
        if conn.status == 'LISTEN':
            open_ports.append({
                "port": conn.laddr.port,
                "address": conn.laddr.ip,
                "status": conn.status
            })
    return open_ports

# Flag security risks
def get_security_risks(data):
    risks = []
    
    # Suspicious ports to watch for
    suspicious_ports = [23, 21, 4444, 1337, 31337, 8080]
    for port_info in data.get("open_ports", []):
        if port_info["port"] in suspicious_ports:
            risks.append({
                "type": "suspicious_port",
                "detail": f"Suspicious port open: {port_info['port']}"
            })
    
    # Suspicious process names
    suspicious_processes = ["netcat", "nc", "nmap", "mimikatz", "meterpreter"]
    for proc in data.get("processes", []):
        if proc["name"].lower() in suspicious_processes:
            risks.append({
                "type": "suspicious_process",
                "detail": f"Suspicious process running: {proc['name']}"
            })
    
    if not risks:
        risks.append({"type": "clean", "detail": "No obvious risks detected"})
    
    return risks
