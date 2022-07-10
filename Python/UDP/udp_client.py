import socket

IP = "127.0.0.1"  # ip (localhost)
PORT = 1234
address = (IP, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    mail = input("Enter a mail ")
    mail = mail.encode("utf-8")
    client.sendto(mail, address)
    mail, address = client.recvfrom(1024)
    mail = mail.decode("utf-8")
    print(f"Server: {mail} ")
