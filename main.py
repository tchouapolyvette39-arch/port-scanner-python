# ================================
# main.py
# Point d'entrée principal
# ================================

from scanner import scan_ports
from utils import (
    validate_ip,
    validate_port_range,
    display_banner,
    resolve_hostname
)

import sys

def main():

    display_banner()

    try:
        target = input("Entrez l'adresse IP ou le nom d'hôte : ").strip()

        # Résolution DNS
        target_ip = resolve_hostname(target)

        if not validate_ip(target_ip):
            print("[ERREUR] Adresse IP invalide.")
            sys.exit(1)

        start_port = int(input("Port de début : "))
        end_port = int(input("Port de fin : "))

        if not validate_port_range(start_port, end_port):
            print("[ERREUR] Plage de ports invalide.")
            sys.exit(1)

        print(f"\n[INFO] Scan en cours sur {target_ip}...\n")

        open_ports = scan_ports(target_ip, start_port, end_port)

        print("\n========== RESULTATS ==========")

        if open_ports:
            for port, service in open_ports:
                print(f"[OUVERT] Port {port} -> Service : {service}")
        else:
            print("Aucun port ouvert détecté.")

        print("\n[INFO] Résultats sauvegardés dans scan_results.txt")

    except KeyboardInterrupt:
        print("\n[INFO] Scan interrompu par l'utilisateur.")
        sys.exit(0)

    except ValueError:
        print("[ERREUR] Veuillez entrer des nombres valides.")

    except Exception as e:
        print(f"[ERREUR INATTENDUE] {e}")


if __name__ == "__main__":
    main()
