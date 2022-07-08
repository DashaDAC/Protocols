import socket

IP = "127.0.0.1"  # ip (localhost)
PORT = 1234  # Port to listen

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((IP, PORT))

while True:
    mail, address = server.recvfrom(1024)
    mail = mail.decode("utf-8")
    print(mail)
    mail = mail.encode("utf-8")

    server.sendto(mail, address)


