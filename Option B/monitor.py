import psutil
import json
import requests
import socket
from datetime import datetime

def check_system_health():
    # 1. Get Metrics
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    # 2. Structure the Data (JSON is industry standard)
    report = {
        "timestamp": datetime.now().isoformat(),
        "hostname": socket.gethostname(),
        "status": "HEALTHY",
        "metrics": {
            "cpu_percent": cpu_usage,
            "memory_percent": memory.percent,
            "disk_free_gb": round(disk.free / (1024**3), 2)
        }
    }

    # 3. Decision Logic (The "Engineering" part)
    if cpu_usage > 80 or memory.percent > 90:
        report["status"] = "CRITICAL"
        # In a real job, you'd trigger a PagerDuty alert here
        print(f"ALERT: High load detected! {report}")
    
    return report

if __name__ == "__main__":
    print(json.dumps(check_system_health(), indent=4))
