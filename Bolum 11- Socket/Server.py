import socket

#ipv4 formatında olan sabit.  /  TCP protokolüne karşılık gelir.
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#HOST="127.0.0.1"    HOST adresini yazdırır.
HOST=socket.gethostbyname(socket.gethostname())
print(HOST)
PORT=12345


server_socket.bind((HOST,PORT))

server_socket.listen()

while True:
    client_socket, client_adress=server_socket.accept()
    print(f"bağlantı yapıldı: {client_adress}")

    print(client_socket)
    print(client_adress)
    break