# Basic Network Analysis

## Introduction

The Internet Control Message Protocol (ICMP) is a foundational protocol in networking used for diagnostic and error-reporting purposes. It plays a key role in tools like "ping," which test connectivity between devices. While simple, ICMP can be used in creative ways to demonstrate networking concepts and cybersecurity techniques.

In this lab, you will use the ping command and Wireshark to analyze ICMP echo reply packets from a target server. The goal is to discover a hidden flag embedded in the replies.

## Understanding ICMP

- How ICMP Works:
	- ICMP helps devices communicate diagnostic messages.
	- The ICMP echo request (type 8) is used to check if a device is reachable.
	- The ICMP echo reply (type 0) responds to such requests, often including payload data.

- ICMP and Payloads:
	- ICMP packets can include a payload that carries arbitrary data.
	- This makes ICMP useful for experiments, diagnostics, and even covert communication.


## Objective of the lab

- The goal of this lab is to uncover a hidden flag embedded in the payload of ICMP echo replies sent by a server. You will:
	- Use the `ping` command to communicate with the target server.
	- Capture and analyze the ICMP replies using Wireshark.
	- Extract the hidden flag from the payload of the echo replies.

## What we will learn

- By the end of this lab, you will:
	- Understand how ICMP echo requests and replies work.
	- Gain experience using Wireshark to capture and analyze network traffic.
	- Learn how payload data in network protocols can carry hidden information.
	- Appreciate the importance of analyzing seemingly "safe" network protocols for hidden data.


## Lab Instructions

- Step 1: Set Up Wireshark
	- Launch Wireshark on your machine.
	- Start capturing packets on the network interface connected to the target server.
	- Apply a display filter: icmp to view only ICMP packets.

- Step 2: Send ICMP Requests
	- Open a terminal.
	- Use the `ping` command to send echo requests to the target server
	- Observe the ICMP echo replies coming back from the server in Wireshark.

- Step 3: Analyze the Replies
	- In Wireshark, select an ICMP echo reply packet.
	- Inspect the payload of the packet in the packet details or hex view.
	- Look for human-readable text in the payload (data), which contains the flag.

- Step 4: Capture the Flag
	- Extract the flag from the payload.
	- Record your findings and verify the flag with Mr. Sako / Aubord.











