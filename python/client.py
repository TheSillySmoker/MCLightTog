import socket
import RPi.GPIO as GPIO
import time

ledPin = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setwarnings(False)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.29", 1234))

while 1:
    msg = s.recv(1024)
    print(msg.decode("utf-8"))

