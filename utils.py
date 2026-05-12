# ================================
# utils.py
# Fonctions utilitaires
# ================================

import socket


def display_banner():

    print("=" * 50)
    print("      PORT SCANNER SECURISE")
    print("   Audit Réseau & Cybersécurité")
    print("=" * 50)


def validate_ip(ip):

    try:
        socket.inet_aton(ip)
        return True

    except socket.error:
        return False


def validate_port_range(start_port, end_port):

    if 1 <= start_port <= 65535 and 1 <= end_port <= 65535:

        if start_port <= end_port:
            return True

    return False


def resolve_hostname(hostname):

    try:
        return socket.gethostbyname(hostname)

    except socket.gaierror:
        return hostname
