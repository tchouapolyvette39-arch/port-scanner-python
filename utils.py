import socket

def valider_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except:
        return False

def parse_ports(ports):
    debut, fin = ports.split("-")
    debut = int(debut)
    fin = int(fin)

    if debut < 0 or fin > 65535 or debut > fin:
        raise ValueError("Ports invalides")

    return debut, fin