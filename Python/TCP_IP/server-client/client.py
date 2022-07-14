import socket

IP = "127.0.0.1"  # ip (localhost)
PORT = 1234  # Port to listen

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((IP, PORT))
mail = input("Enter:")
server.send(bytes(mail, "utf-8"))
buffer = server.recv(1024)
buffer = buffer.decode("utf-8")
print(f"Server: {buffer}")