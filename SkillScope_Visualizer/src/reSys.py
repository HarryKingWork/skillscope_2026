import subprocess
import platform
from sys import platform
import sys
import psutil
import shutil
#import speedtest

# Function to detect OS
def detect_os():
    system = platform.system().lower()
    if system == 'linux':
        return "Linux"
    elif system == 'darwin':
        return "macOS"
    elif system == 'windows':
        return "Windows"
    else:
        return "Unknown OS"

# Function to get system info
def get_system_info():
    info = {
        'platform': platform.platform(),
        'architecture': platform.architecture(),
        'processor': platform.processor(),
        'os': detect_os(),
        'python_version': platform.python_version(),
    }
    return info

# Function to check if a command exists
def command_exists(command):
    return shutil.which(command) is not None
    

# Function to install a package (cross-platform)
def install_package(package_name):
    os_name = detect_os()
    if os_name == "Linux":
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
    elif os_name == "macOS":
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
    elif os_name == "Windows":
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

# Function to check disk space
def check_disk_space():
    disk = psutil.disk_usage('/')
    return disk

# Function to check memory usage
def check_memory_usage():
    memory = psutil.virtual_memory()
    return memory

# Function to check CPU usage
def check_cpu_usage():
    cpu = psutil.cpu_percent(interval=1)
    return cpu

# Function to check if Docker is running
def check_docker():
    if command_exists("docker"):
        try:
            result = subprocess.run(['docker', 'info'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                return "Docker is running."
            else:
                return "Docker is not running."
        except Exception as e:
            return str(e)
    else:
        return "Docker is not installed."

# Function to check if Kubernetes is installed
def check_kubernetes():
    if command_exists("kubectl"):
        try:
            result = subprocess.run(['kubectl', 'version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                return "Kubernetes is installed."
            else:
                return "Kubernetes is not installed."
        except Exception as e:
            return str(e)
    else:
        return "Kubernetes is not installed."

# Function to run system tests
def run_system_tests():
    tests = {
        "System Info": get_system_info(),
        "Disk Space": check_disk_space(),
        "Memory Usage": check_memory_usage(),
        "CPU Usage": check_cpu_usage(),
        "Docker Status": check_docker(),
        "Kubernetes Status": check_kubernetes()
    }

    for test, result in tests.items():
        print(f"{test}: {result}")

# Function to check if a process is running
def check_process(process_name):
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if process_name.lower() in proc.info['name'].lower():
            return f"Process {process_name} is running (PID: {proc.info['pid']})"
    return f"Process {process_name} is not running."

# Function to stop a process
def stop_process(process_name):
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if process_name.lower() in proc.info['name'].lower():
            proc.terminate()
            return f"Terminated process {process_name} (PID: {proc.info['pid']})"
    return f"Process {process_name} not found."

# Function to restart a service (for Linux/macOS)
def restart_service(service_name):
    os_name = detect_os()
    if os_name in ["Linux", "macOS"]:
        try:
            subprocess.check_call(['sudo', 'systemctl', 'restart', service_name])
            return f"{service_name} service restarted successfully."
        except subprocess.CalledProcessError as e:
            return f"Failed to restart {service_name}: {e}"
    else:
        return "Service restart is not supported on Windows."

# Function to create a basic web server for testing
def start_simple_web_server():
    os_name = detect_os()
    if os_name == "Linux" or os_name == "macOS":
        subprocess.Popen(['python3', '-m', 'http.server', '8080'])
    elif os_name == "Windows":
        subprocess.Popen(['python', '-m', 'http.server', '8080'])
    return "Web server started on port 8080."
    
# Function to check if a port is open
def check_port_open(port):
    if command_exists("nc"):
        try:
            result = subprocess.run(['nc', '-zv', 'localhost', str(port)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                return f"Port {port} is open."
            else:
                return f"Port {port} is closed."
        except Exception as e:
            return str(e)
    else:
        return "nc (netcat) is not installed."