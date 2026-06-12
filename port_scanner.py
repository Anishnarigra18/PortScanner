import socket
from datetime import datetime

target = input("Enter IP address to scan: ")

print("-" * 50)
print(f"Scanning Target: {target}")
print(f"Started at: {datetime.now()}")
print("-" * 50)

open_ports = []

for port in range(8000, 8101):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.3)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"[OPEN] Port {port}")
        open_ports.append(port)

    sock.close()

print("\n" + "-" * 50)
print("SCAN COMPLETE")
print("-" * 50)

print(f"Total Open Ports: {len(open_ports)}")

if open_ports:
    print("Open Ports Found:")
    for port in open_ports:
        print(port)

else:
    print("No Open Ports Found")
