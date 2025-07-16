import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 8888))

print("UDP Server: Waiting for data...")
data, addr = server_socket.recvfrom(1024)
print(f"UDP Server: Received -> {data.decode()} from {addr}")
