import os
import sys
import platform
import subprocess
import socket
import time
import shutil
import psutil
import tempfile
import hashlib

# Helper functions for various tests
def check_os():
    """Check the operating system."""
    return platform.system()

def check_python_version():
    """Check Python version."""
    return sys.version

def check_disk_space():
    """Check the disk space on the current drive."""
    total, used, free = shutil.disk_usage("/")
    return total, used, free

def check_cpu_usage():
    """Check CPU usage percentage."""
    return psutil.cpu_percent(interval=1)

def check_memory_usage():
    """Check memory usage."""
    memory = psutil.virtual_memory()
    return memory.percent

def check_process_list():
    """Check running processes."""
    processes = [p.info for p in psutil.process_iter(['pid', 'name'])]
    return processes

def check_network_connections():
    """Check active network connections."""
    connections = psutil.net_connections(kind='inet')
    return connections

def check_system_uptime():
    """Check system uptime."""
    uptime = time.time() - psutil.boot_time()
    return uptime

def check_python_modules_installed():
    """Check installed Python modules."""
    installed_modules = list(sys.modules.keys())
    return installed_modules

def check_file_exists(file_path):
    """Check if a file exists."""
    return os.path.exists(file_path)

def create_temp_file():
    """Create a temporary file."""
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(b"Temporary file content")
    temp_file.close()
    return temp_file.name

def delete_temp_file(file_path):
    """Delete a temporary file."""
    os.remove(file_path)

def check_port_open(port):
    """Check if a specific port is open."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('localhost', port))
    sock.close()
    return result == 0

def check_file_permissions(file_path):
    """Check file permissions."""
    return os.access(file_path, os.R_OK | os.W_OK | os.X_OK)

def check_user_home():
    """Check the home directory of the current user."""
    return os.path.expanduser("~")

def check_environment_variables():
    """Check if certain environment variables are set."""
    return os.environ

def check_path():
    """Check if the executable is in the system path."""
    return os.getenv("PATH")

def check_internet_connection():
    """Check internet connection by pinging google.com."""
    try:
        response = subprocess.check_call(['ping', '-c', '1', 'google.com'])
        return True
    except subprocess.CalledProcessError:
        return False

def check_file_type(file_path):
    """Check the type of a file."""
    return os.path.splitext(file_path)[1]

def check_system_info():
    """Get system information."""
    return platform.uname()

def check_docker_running():
    """Check if Docker is running."""
    try:
        result = subprocess.check_output(['docker', 'info'])
        return "Docker is running"
    except subprocess.CalledProcessError:
        return "Docker is not running"

def check_git_installed():
    """Check if Git is installed."""
    try:
        subprocess.check_output(['git', '--version'])
        return True
    except subprocess.CalledProcessError:
        return False

def check_process_exists(process_name):
    """Check if a specific process is running."""
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            return True
    return False

def check_file_size(file_path):
    """Check the size of a file."""
    return os.path.getsize(file_path)

def check_file_hash(file_path):
    """Generate the hash of a file."""
    hash_md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def check_ping(host):
    """Check ping to a remote host."""
    response = os.system(f"ping -c 1 {host}")
    return response == 0

def check_service_status(service_name):
    """Check if a service is running (Linux only)."""
    if check_os() == 'Linux':
        result = subprocess.run(['systemctl', 'is-active', service_name], stdout=subprocess.PIPE)
        return result.stdout.decode().strip()
    else:
        return "Service check only works on Linux."

def check_memory_swap():
    """Check system swap usage."""
    swap = psutil.swap_memory()
    return swap.percent

def check_cpu_temperature():
    """Check CPU temperature (Linux only)."""
    if check_os() == 'Linux':
        try:
            with open('/sys/class/thermal/thermal_zone0/temp') as f:
                temp = int(f.read()) / 1000.0
            return temp
        except FileNotFoundError:
            return "Temperature not available."
    else:
        return "CPU temperature check only works on Linux."

def check_docker_version():
    """Check Docker version."""
    try:
        result = subprocess.check_output(['docker', '--version'])
        return result.decode()
    except subprocess.CalledProcessError:
        return "Docker is not installed"

def check_system_load():
    """Check the system load average."""
    load = os.getloadavg()
    return load

def check_process_cpu_usage(pid):
    """Check CPU usage of a process by PID."""
    try:
        process = psutil.Process(pid)
        return process.cpu_percent(interval=1)
    except psutil.NoSuchProcess:
        return f"Process {pid} not found"

def check_system_memory():
    """Check system memory."""
    return psutil.virtual_memory()

def check_checkin_service(service_name):
    """Check the status of a service (Windows only)."""
    if check_os() == 'Windows':
        result = subprocess.run(['sc', 'qc', service_name], stdout=subprocess.PIPE)
        return result.stdout.decode().strip()
    else:
        return "Service check only works on Windows."