import socket

PORT=12345
SERVER=socket.gethostbyname(socket.gethostname())
ADRESS=(SERVER,PORT)
FORMAT="utf-8"
BYTESIZE=1024
DISCONNECT_MESSAGE="quit"

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADRESS)

while True:
    message=client.recv(BYTESIZE).decode(FORMAT)

    if message==DISCONNECT_MESSAGE:
        client.send("çıkış yapıldı.".encode(FORMAT))
        break
    else:
        print(f"{message}\n")
        message=input("mesaj: ")
        client.send(message.encode(FORMAT))
client.close()