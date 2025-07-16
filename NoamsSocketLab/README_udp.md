# Noam's Cyber Lab

This repo is a collection of hands-on cybersecurity and networking projects I'm building as I prepare for the CompTIA Security+ certification. Everything here is designed to reinforce core concepts through actual code, not just theory.

## TCP Socket Demo (Python)

A simple client-server program using TCP sockets to simulate how devices connect, send, and receive messages over a network. Good intro to how the TCP handshake works and how ports are used.

### Files:
- `tcp_server.py` — waits for incoming TCP connections and replies
- `tcp_client.py` — connects to the server and sends a message

### How to run:
1. Open two terminals
2. In one, run the server:
   ```
   python tcp_server.py
   ```
3. In the other, run the client:
   ```
   python tcp_client.py
   ```
You’ll see the server accept the connection and respond to the client.

### What it demonstrates:
- TCP handshake in action
- Basic socket programming
- Localhost and port usage
- Foundation for future tools like port scanners, listeners, or basic intrusion detection scripts

---

### What’s next:
- UDP version of this demo
- Port scanner script
- Syslog parser for log analysis
- Security-focused mini scripts using Python

This repo will keep growing over time as I learn and build more.

## UDP Socket Demo (Python)

This project builds on the TCP example and demonstrates how UDP communication works using Python. Unlike TCP, UDP doesn't guarantee delivery, order, or even a connection. It's lightweight and fast, but less reliable.

### Files:
- `udp_server.py` — waits for a UDP datagram on port 8888
- `udp_client.py` — sends a one-way message to the server

### How to run:
1. Open two terminals
2. In one, run the server:
   ```
   python udp_server.py
   ```
3. In the other, run the client:
   ```
   python udp_client.py
   ```
The client sends a message, and the server receives it — no handshake, no response. That’s UDP.

### What it demonstrates:
- UDP's “fire and forget” behavior
- No connection needed to send data
- Good for understanding DNS, VoIP, and streaming protocols
- Comparison point against TCP for Security+ topics like reliability and attack surfaces
