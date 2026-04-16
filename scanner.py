import socket
import time

def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    try:
        s.connect((ip, port))
        s.close()
        return True
    except:
        return False

def scan_ports(ip, debut, fin):
    open_ports = []

    for port in range(debut, fin + 1):
        print(f"Scan du port {port}...")

        if scan_port(ip, port):
            print(f" Port {port} ouvert")
            open_ports.append(port)

        time.sleep(0.3)

    return open_ports