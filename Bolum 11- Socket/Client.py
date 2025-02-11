import socket

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST=socket.gethostbyname(socket.gethostname())
print(HOST)
PORT=12345
client_socket.connect(HOST,PORT)