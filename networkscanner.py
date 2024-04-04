from scapy.all import ARP, Ether, srp

def scan_network(target_ip, timeout):
    # Create an ARP request packet
    arp = ARP(pdst=target_ip)
    # Create an Ethernet frame around the ARP request packet
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    # Combine the Ethernet frame and the ARP request packet
    packet = ether/arp

    # Use Scapy's srp() function to send the packet and receive a response
    result = srp(packet, timeout=timeout, verbose=False)[0]

    # Extract the IP and MAC addresses from the response
    clients = []
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})

    return clients

if __name__ == "__main__":
    target_ip = input("Enter the target IP address (e.g. 192.168.0.0/24): ")
    timeout = float(input("Enter the timeout (in seconds) for the ARP requests (default: 2 seconds): ") or 2)

    print(f'Scanning network {target_ip}...')
    clients = scan_network(target_ip, timeout)
    print('Connected devices:')
    for client in clients:
        print(f'IP: {client["ip"]}\tMAC: {client["mac"]}')
