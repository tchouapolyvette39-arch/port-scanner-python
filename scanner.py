# ================================
# scanner.py
# Logique de scan réseau
# ================================

import socket
import time

TIMEOUT = 1

def get_service_name(port):

    common_services = {
        20: "FTP Data",
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        67: "DHCP",
        68: "DHCP",
        80: "HTTP",
        110: "POP3",
        123: "NTP",
        143: "IMAP",
        161: "SNMP",
        179: "BGP",
        443: "HTTPS",
        3306: "MySQL",
        3389: "RDP",
        5432: "PostgreSQL",
        8080: "HTTP Proxy"
    }

    return common_services.get(port, "Service inconnu")


def save_results(results):

    with open("scan_results.txt", "w") as file:

        file.write("===== RESULTATS DU SCAN =====\n\n")

        for port, service in results:
            file.write(f"Port {port} ouvert -> {service}\n")


def scan_ports(target_ip, start_port, end_port):

    open_ports = []

    for port in range(start_port, end_port + 1):

        try:

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(TIMEOUT)

            result = sock.connect_ex((target_ip, port))

            if result == 0:

                service = get_service_name(port)

                print(f"[+] Port {port} OUVERT ({service})")

                open_ports.append((port, service))

            sock.close()

            # Simulation réaliste
            time.sleep(0.1)

        except socket.error:
            print(f"[ERREUR] Impossible de scanner le port {port}")

    save_results(open_ports)

    return open_ports
