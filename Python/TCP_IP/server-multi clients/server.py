import socket
import threading

def hangle_client(client, address):
    print(f"[NEW CONNECTIONS] {address} connected")

    connected = True
    while connected:
        mail = client.recv(1024)
        mail = mail.decode("utf-8")
        if mail == DISCONNECT_MAIL:
            connected = False
        print(mail)
        client.send(bytes(mail, "utf-8"))

    client.close()



IP = socket.gethostbyname(socket.gethostname())
PORT = 1234  # Port to listen
DISCONNECT_MAIL = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(5)
while True:
    client, address = server.accept()
    thread = threading.Thread(target=hangle_client, args=(client, address))
    thread.start()
    print(f"Connected by {address[0]}:{address[1]}")
    print(f"active connections {threading.activeCount()-1}")



    # mail = client.recv(1024)
    # mail = mail.decode("utf-8")
    # print(mail)
    # client.send(bytes(mail, "utf-8"))
    #
    # client.close()
