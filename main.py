from icmplib import ping, multiping
from ipaddress import ip_address, ip_network

def discovery_network(ip):
    ips_network = [str(ip) for ip in ip.hosts()]
    host_live = multiping(ips_network,  count=1, timeout=2, interval=1)
    for ip in host_live:
        if ip.is_alive:
            print(f"Host activo. {ip.address}, con un promedio en envio de {ip.avg_rtt} con {ip.packets_sent} paquetes enviados")


def discovery_host(ip):
    ip_str = str(ip)
    host_objetivo =ping(ip_str, count=1, timeout=2, interval=1)
    
    if host_objetivo.is_alive:
        print(f"[+] Host Live: {ip.address} | RTT: {ip.avg_rtt}ms | Sent: {ip.packets_sent}")
    else:
        print("Sin respuesta")


ip_obj = input("Ingresa una ip: ")

try:
    if "/" in ip_obj:
        ip_valida = ip_network(ip_obj)
        discovery_network(ip_valida)
        
    else:
        ip_valida = ip_address(ip_obj)
        discovery_host(ip_valida)
except:
    print("Ingresa una IP valida o una RED valida")
