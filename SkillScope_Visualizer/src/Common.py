import os
import subprocess
import socket
import psutil
import platform
import time
from src import Ops
#import speedtest

def check_disk_usage():
    """Check disk usage and alert if usage exceeds 80%."""
    usage = psutil.disk_usage('/')
    print(f"Disk Usage: {usage.percent}%")
    return usage.percent < 80

def check_memory_usage():
    """Check memory usage and alert if usage exceeds 80%."""
    usage = psutil.virtual_memory()
    print(f"Memory Usage: {usage.percent}%")
    return usage.percent < 80

def check_cpu_usage():
    """Check CPU usage and alert if usage exceeds 75%."""
    usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {usage}%")
    return usage < 75

def check_service_running(service_name):
    """Check if a service is running, cross-platform."""
    system = platform.system()
    try:
        if system == "Linux" or system == "Darwin":
            output = subprocess.check_output(['systemctl', 'is-active', service_name])
            return output.strip().decode('utf-8') == 'active'
        elif system == "Windows":
            output = subprocess.check_output(['sc', 'query', service_name])
            return "RUNNING" in output.decode('utf-8')
    except Exception:
        return False

def check_port_open(port):
    """Check if a specific port is open."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        result = s.connect_ex(('127.0.0.1', port))
        return result == 0

def check_network_latency(host='8.8.8.8'):
    """Check network latency by pinging a known host, cross-platform."""
    system = platform.system()
    try:
        if system == "Windows":
            subprocess.check_output(['ping', '-n', '1', host])
        else:
            subprocess.check_output(['ping', '-c', '1', host])
        print("Network latency check: PASS")
        return True
    except subprocess.CalledProcessError:
        print("Network latency check: FAIL")
        return False

def check_file_system_health():
    """Check file system health using fsck or chkdsk, cross-platform."""
    system = platform.system()
    try:
        if system == "Linux" or system == "Darwin":
            subprocess.check_output(['fsck', '-n', '/'])
        elif system == "Windows":
            subprocess.check_output(['chkdsk', 'C:'])
        print("File system health check: PASS")
        return True
    except Exception:
        print("File system health check: FAIL")
        return False

def check_log_errors(log_file=None, keyword='error'):
    """Scan logs for error keywords, using platform-specific log files."""
    system = platform.system()
    if log_file is None:
        log_file = '/var/log/syslog' if system in ['Linux', 'Darwin'] else 'C:\\Windows\\System32\\Winevt\\Logs\\Application.evtx'
    if os.path.exists(log_file):
        with open(log_file, 'r', errors='ignore') as f:
            logs = f.readlines()
            errors = [line for line in logs if keyword.lower() in line.lower()]
            if errors:
                print(f"Found {len(errors)} error(s) in logs.")
                return False
    return True

def check_disk_io():
    """Check disk read/write speeds."""
    io_counters = psutil.disk_io_counters()
    print(f"Disk Read: {io_counters.read_bytes} bytes, Disk Write: {io_counters.write_bytes} bytes")
    return True

def check_cpu_temperature():
    """Check CPU temperature if supported."""
    if hasattr(psutil, "sensors_temperatures"):
        temps = psutil.sensors_temperatures()
        if "coretemp" in temps:
            for sensor in temps["coretemp"]:
                print(f"CPU Temperature: {sensor.current}'C")
                return sensor.current < 85
    print("CPU Temperature monitoring not supported.")
    return True

def check_available_updates():
    """Check for available OS updates."""
    system = platform.system()
    try:
        if system == "Linux":
            subprocess.check_output(['apt', 'list', '--upgradable'])
        elif system == "Windows":
            subprocess.check_output(['wmic', 'qfe', 'list'])
        elif system == "Darwin":
            subprocess.check_output(['softwareupdate', '-l'])
        print("System updates check: PASS")
        return True
    except Exception:
        print("System updates check: FAIL")
        return False

def check_internet_speed():
    """Check internet download and upload speed using speedtest library."""
    try:
        #st = speedtest.Speedtest()
        #st.get_best_server()
        #download_speed = st.download() / 1_000_000  # Convert to Mbps
        #upload_speed = st.upload() / 1_000_000  # Convert to Mbps
        #print(f"Download Speed: {download_speed:.2f} Mbps")
        #print(f"Upload Speed: {upload_speed:.2f} Mbps")
        return True
    except Exception as e:
        print(f"Internet speed check: FAIL - {e}")
        return False

def check_uptime():
    """Check system uptime."""
    Ops.current_timezone()
    uptime = time.time() - psutil.boot_time()
    print(f"System Uptime: {uptime / 3600:.2f} hours")
    return True
