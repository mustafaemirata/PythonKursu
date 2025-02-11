import socket

PORT=12345
SERVER=socket.gethostbyname(socket.gethostname())
ADRESS=(SERVER,PORT)
FORMAT="utf-8"
BYTESIZE=1024
DISCONNECT_MESSAGE="quit"

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADRESS)

#Hattı dinleme moduna geçiş yapıldı.
server.listen()
print("server çalışıyor...\n")

client_socket,client_adress=server.accept()

#Belirlenen formatta encode ederek clinet'e gönderim.
client_socket.send("server bağlantısı yapıldı.\n".encode(FORMAT))

while True:
    message = client_socket.recv(BYTESIZE).decode(FORMAT)

    if message == DISCONNECT_MESSAGE:
        client_socket.send("çıkış yapıldı.".encode(FORMAT))
        break
    else:
        print(f"{message}\n")
        message = input("mesaj: ")
        client_socket.send(message.encode(FORMAT))
server.close()
