import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.sendto("Hello UDP Server!".encode(), ('localhost', 8888))

print("UDP Client: Message sent!")
