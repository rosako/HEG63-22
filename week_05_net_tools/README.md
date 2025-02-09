# Network tools 101

## Wireshark 101

### Task 1
- Start Wireshark and capture on the interface that connects to the Internet.
- Issue `arp -a` command on the command line
- Find the hosts living in the same LAN


### Task 2
- With Wireshark open
- Send a ping to any IP address of your choice, once from Windows, once from your Linux VM.
- What are the payloads used in each case?


## Nmap 101

### Task 1
- Connect to our local hacklab
- Scan the network to get a simple list of the live hosts


### Task 2
- Do a complete scan the two hosts indicated by the teacher
- Identify which services are open



## Scapy 101

### Task 1
- Use scapy to send a ping to your default gateway
- Observe what is going on using wireshark


### Task 2
- Leave wireshark open and sniffing
- Send a ping to the default gateway, pretending to be another host
- On the usurpated host, leave wireshark running and check what you receive
