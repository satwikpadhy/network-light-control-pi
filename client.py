#!/usr/bin/python
import socket
import os
val=0
port = 12345

def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')


while(val!='2'):
    screen_clear()
    print("Control Lights\nTurn On : Enter '1'\nTurn Off : Enter '0'\nExit the Application : Enter '2'")
    s = socket.socket()
    s.connect(('192.168.29.190', port))
    #192.168.29.190 is the address of my raspberrypi in my network
    #change it according to your setup
    val = str(input())
    s.send(val)
    s.close()
