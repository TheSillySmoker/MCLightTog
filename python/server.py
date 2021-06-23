import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.1.29", 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    while 1:
        try:
             clientsocket.send(bytes(input("Please enter a message: "), "utf-8"))
             msg = s.recv(1024)
             print(msg.decode("utf-8"))
        except: 
            print(f"{address}has left the server")
            clientsocket, address = s.accept()
        
       
