import socket
import sys

# Runs through each port from start_port to end_port
def scan_ports(ip, start_port, end_port):
    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(2)
                result = s.connect_ex((ip, port))
                service_name = port_name_service(port)

                if result == 0:
                    print(f"{ip} : Open port: {port}, Service: {service_name}", file=sys.stdout)

        except Exception as e:
            print(f"Error occurred while scanning port {port}: {e}", file=sys.stderr)

# Obtains the service name if available
def port_name_service(port):
    try:
        return socket.getservbyport(port, "tcp")
    except Exception as e:
        return "unknown"

# Ask user for IP address and port range
ip_address = input("Enter the IP address: ")
port_range = input("Enter the port range (e.g., start:end): ")

start_port, end_port = map(int, port_range.split(":"))

if start_port < 1 or start_port > 65535 or end_port < 1 or end_port > 65535 or start_port > end_port:
    print("Invalid port range", file=sys.stderr)
    sys.exit(1)

# Perform port scanning
try:
    scan_ports(ip_address, start_port, end_port)
except Exception as e:
    print(f"Error occurred during port scanning: {e}", file=sys.stderr)
