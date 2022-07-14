import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 1234  # Port to listen
DISCONNECT_MAIL = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))
print(f"Client connected to server {IP}:{PORT}")
connected = True
while connected:
    mail = input("> ")
    client.send(mail.encode("utf-8"))
    if mail == DISCONNECT_MAIL:
        connected = False
    else:
        mail = client.recv(1024).decode("utf-8")
        print(f"[SERVER] {mail}")


    # mail = client.recv(1024)
    # mail = mail.decode("utf-8")
    # print(mail)
    # client.send(bytes(mail, "utf-8"))
    #
    # client.close()
