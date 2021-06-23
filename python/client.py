import socket
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)   
ledPin = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.29", 1234))

while 1:
    msg = s.recv(1024)
    print(msg.decode("utf-8")) 
    decMsg = msg.decode("uft-8")
    if (decMsg == "On"):
        GPIO.output(ledPin, GPIO.HIGH)
    if (decMsg == "Off"):
        GPIO.output(ledPin, GPIO.LOW)
    if(decMsg == "Flash"):
        i = 0
        while i < 10:
            GPIO.output(ledPin, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(ledPin, GPIO.LOW)
            time.sleep(0.5)
            i = i + 1

