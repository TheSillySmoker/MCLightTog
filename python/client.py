import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.29", 1234))

while 1:
    msg = s.recv(1024)
    print(msg.decode("utf-8"))
    s.send(bytes("Right back at ya bitch!", "utf-8"))