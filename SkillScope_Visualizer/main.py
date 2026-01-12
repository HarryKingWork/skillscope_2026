#import matplotlib.pyplot as plt
from src import Basic, Common

# Main function to execute all tests
def run_basic_tests():
    tests = [
        ("OS", Basic.check_os),
        ("Python Version", Basic.check_python_version),
        ("Create Temp File", Basic.create_temp_file),
        ("Delete Temp File", lambda: Basic.delete_temp_file(Basic.create_temp_file())),
        #("Internet Connection", Basic.check_internet_connection),
        ("System Info", Basic.check_system_info),
        ("Process Running", lambda: Basic.check_process_exists("nginx")),
        ("Ping Test", lambda: Basic.check_ping("google.com")),
        ("Swap Usage", Basic.check_memory_swap),
        ("CPU Temperature", Basic.check_cpu_temperature),
        ("Process CPU Usage", lambda: Basic.check_process_cpu_usage(1234)),
        ("System Memory", Basic.check_system_memory),
    ]
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            print(f"{test_name}: {result}")
        except Exception as e:
            print(f"{test_name} failed: {e}")

def run_common_tests():
    tests = {
        "Disk Usage": Common.check_disk_usage(),
        "File System Health": Common.check_file_system_health(),
        "Memory Usage": Common.check_memory_usage(),
        "CPU Usage": Common.check_cpu_usage(),
        "System Uptime": Common.check_uptime(),
        "Nginx Running": Common.check_service_running("nginx"),
        "Port 80 Open": Common.check_port_open(80),
        "Network Latency": Common.check_network_latency(),
        "Disk IO": Common.check_disk_io(),
        "Available Updates": Common.check_available_updates(),
    }
    
    return tests

if __name__ == "__main__":
    tests_common = run_common_tests() 
    test_basic = run_basic_tests()

    test_names = []
    test_results = []

    for test, result in tests_common.items():
        status = 'PASS' if result else 'FAIL'
        print(f"{test}: {status}")
        test_names.append(test)
        test_results.append(1 if result else 0)

    #for test1, result1 in test_basic.items():
    #    status1 = 'PASS' if result else 'FAIL'
    #    print(f"{test1}: {status1}")
    #    test_names.append(test1)
    #    test_results.append(1 if result1 else 0)

    # Plotting the results
    #colors = ['green' if r else 'red' for r in test_results]

    #plt.figure(figsize=(10, 6))
    #bars = plt.barh(test_names, test_results, color=colors)
    #plt.xlabel('Result')
    #plt.title('System Analyse for DevOps')
    #plt.xlim(0, 1.2)
    #plt.xticks([0, 1], ['FAIL', 'PASS'])

    #for bar, result in zip(bars, test_results):
    #    label = 'PASS' if result else 'FAIL'
    #    plt.text(bar.get_width() + 0.05, bar.get_y() + bar.get_height()/2,
    #             label, va='center', ha='left', fontsize=10)

    #plt.tight_layout()
    #plt.show()