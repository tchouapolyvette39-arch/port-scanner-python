from scanner import scan_ports
from utils import valider_ip, parse_ports

def main():
    print("=== SCANNER DE PORTS ===")

    ip = input("Entrer l'adresse IP : ")

    if not valider_ip(ip):
        print("Adresse IP invalide")
        return

    ports = input("Entrer la plage de ports (ex: 20-100) : 
    try:
        debut, fin = parse_ports(ports)
    except:
        print("Plage de ports invalide")
        return

    print(f"\n Scan de {ip} de {debut} à {fin}...\n")

    open_ports = scan_ports(ip, debut, fin)

    print("\n Ports ouverts :")
    if open_ports:
        for port in open_ports:
            print(f"- Port {port}")
    else:
        print("Aucun port ouvert trouvé.")

if __name__ == "__main__":
    main()