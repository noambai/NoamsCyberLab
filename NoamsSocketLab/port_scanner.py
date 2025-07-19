import socket
from datetime import datetime

target = input("Enter target IP or hostname: ")
start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")
start_time = datetime.now()

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is OPEN")
    sock.close()

end_time = datetime.now()
print(f"\nScan completed in: {end_time - start_time}")
