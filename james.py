import os
import platform
import socket
import datetime
import json

def get_system_info():
    """Collect system information using built-in libraries."""
    system_info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "OS Release": platform.release(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Architecture": platform.architecture(),
        "Hostname": socket.gethostname(),
        "IP Address": socket.gethostbyname(socket.gethostname()),
        "Current Directory": os.getcwd(),
        "Python Version": platform.python_version(),
        "Python Build": platform.python_build(),
    }
    return system_info

def write_to_file(filename, data):
    """Write the collected information to a file."""
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"System information written to {filename}")
    except IOError as e:
        print(f"Error writing to file: {e}")

def main():
    print("Collecting system information...")
    system_info = get_system_info()
    print("System Information:")
    for key, value in system_info.items():
        print(f"{key}: {value}")
    
    # Save to a file
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"system_info_{current_time}.json"
    write_to_file(filename, system_info)

if __name__ == "__main__":
    main()
