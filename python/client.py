import socket


TCP_IP = '192.168.1.19' # this IP of my pc. When I want raspberry pi 2`s as a client, I replace it with its IP '169.254.54.195'
TCP_PORT = 8123
BUFFER_SIZE = 1024


while 1:
        
    MESSAGE = "Please enter your message: "

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(str(MESSAGE))
    data = s.recv(BUFFER_SIZE)
    s.close()

    print ("received data:", data)
