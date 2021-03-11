#!/usr/bin/python
import socket
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

s = socket.socket()
print ("Socket successfully created")
port = 12345
s.bind(('', port))
print ("socket binded to %s" %(port))
s.listen(5)
print ("socket is listening")

while True:
    data = 0
    c, addr = s.accept()
    print ('Got request from', addr )
    data = c.recv(1024)
    print("Request :", data)
    if(data == '1'):
        GPIO.output(8, GPIO.HIGH)
    else:
        GPIO.output(8, GPIO.LOW)
    c.close()
