import socket

services = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    8080: "HTTP-ALT"
}

target = input("Enter IP Address: ")

print("\nScanning:", target)
print("-" * 50)

for port in [21, 22, 23, 25, 53, 80, 110, 143, 443, 8080]:

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"\n[OPEN] Port {port}")
            print(f"Service: {services.get(port, 'Unknown')}")

            try:
                banner = sock.recv(1024).decode().strip()

                if banner:
                    print("Banner:", banner)
                else:
                    print("Banner: Not Available")

            except:
                print("Banner: Not Available")

        sock.close()

    except:
        pass

print("\nScan Complete")
