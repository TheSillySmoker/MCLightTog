import socket
import RPi.GPIO as GPIO
import time

ledPin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.29", 1234))

while 1:
    msg = s.recv(1024)
    decMsg = msg.decode("utf-8")
    print(msg.decode("utf-8"))
    if (decMsg == "On"):
        GPIO.output(ledPin, GPIO.HIGH)
    if (decMsg == "Off"):
        GPIO.output(ledPin, GPIO.LOW)