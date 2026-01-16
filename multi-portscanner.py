import socket
import sys

print("=========================================")
print("Welcome to Multi - PortScanner\n")

# Validate arguments
if len(sys.argv) != 4 or sys.argv[2] != "-p":
    print("Usage: python port_scan.py <ip_or_file.txt> -p <port>")
    sys.exit()

ip_input = sys.argv[1]
port = int(sys.argv[3])

def scan(ip, port):
    ip = ip.strip()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    try:
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"[OPEN ] {ip}:{port}")
        else:
            print(f"[CLOSED] {ip}:{port}")
    except Exception as e:
        print(f"[ERROR] {ip}:{port} -> {e}")
    finally:
        s.close()

# If input is a .txt file
if ip_input.endswith(".txt"):
    with open(ip_input, "r") as f:
        for addr in f.readlines():
            scan(addr, port)
else:
    scan(ip_input, port)

print("\n=========================================")
print("Thanks for using Multi - PortScanner")
print("Developed by sudo_0xksh")