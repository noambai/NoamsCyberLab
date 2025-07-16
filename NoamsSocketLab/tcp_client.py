# tcp_client.py
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 9999))

client_socket.sendall("Hello TCP Server!".encode())
response = client_socket.recv(1024).decode()
print(f"TCP Client: Server replied -> {response}")

client_socket.close()
