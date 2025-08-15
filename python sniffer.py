from scapy.all import sniff, IP, TCP, UDP
def packet_handler(packet): 
    if packet.haslayer(IP):
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        protocol = "Other"
        if packet.haslayer(TCP):
            protocol = "TCP"
        elif packet.haslayer(UDP):
            protocol = "UDP"
        print(f"Protocol: {protocol} | Source IP: {source_ip} | Destination IP: {destination_ip}")
print("Starting network sniffer...")
sniff(prn=packet_handler, count=100)
print("Sniffing finished.")