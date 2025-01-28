from scapy.all import sniff, IP, ICMP, send

# Define the full flag to send in each reply
flag = "HEG_FLAG{PingMeForTheFlag}"

# Function to handle incoming ICMP packets
def handle_packet(packet):
    # Check if it's an ICMP echo request
    if packet.haslayer(ICMP) and packet[ICMP].type == 8:  # Type 8 = Echo Request
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        # Prepare the ICMP echo reply
        icmp_reply = IP(src=dst_ip, dst=src_ip) / ICMP(type=0, id=packet[ICMP].id, seq=packet[ICMP].seq)
        
        # Add the entire flag as the payload
        icmp_reply = icmp_reply / flag.encode()

        # Send the ICMP reply
        send(icmp_reply, verbose=0)

        # Log the event for debugging
        print(f"Sent flag to {src_ip}")

# Start sniffing for ICMP echo requests
print("Listening for ICMP echo requests...")
sniff(filter="icmp", prn=handle_packet)

