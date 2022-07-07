import socket

IP = "127.0.0.1"  # ip (localhost)
PORT = 1234  # Port to listen

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(5)
while True:
    client, address = server.accept()
    print(f"Connected by {address[0]}:{address[1]}")

    mail = client.recv(1024)
    mail = mail.decode("utf-8")
    print(mail)
    client.send(bytes(mail, "utf-8"))

    client.close()
