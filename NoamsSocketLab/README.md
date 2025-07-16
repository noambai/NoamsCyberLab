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
