# tcp_server.py
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 9999))
server_socket.listen(1)
print("TCP Server: Waiting for connection...")

conn, addr = server_socket.accept()
print(f"TCP Server: Connected by {addr}")

data = conn.recv(1024).decode()
print(f"TCP Server: Received -> {data}")
conn.sendall("Message received!".encode())

conn.close()
