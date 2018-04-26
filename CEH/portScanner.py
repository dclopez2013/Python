#!/usr/bin/env python

import socket
import subprocess
import sys
from datetime import datetime

#clear the screen
subprocess.call('CLS', shell=True)

#get user input

print("Enter host to scan:\n")
remoteServer = input()
remoteServerIP = socket.gethostbyname(remoteServer)
socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("remote server ip\n")
print(remoteServerIP)

print("*" * 50)
print("scanning host now")
print("*" * 50)

startTime = datetime.now()

print("scan started at", startTime)


def scanhosts():
    for port in range(0, 10):
        result = socks.connect_ex((remoteServerIP, port))
        if result == True:
            print("Port ", port, " is Open")
        else:
            print("Port ", port, "is not Open")


# for port in range(0,100):
#     result = scanhosts(0,100)
#     if result == None:
#         print("Port ", port, " closed")
#     else:
#         print("Port", port, " open")
#         break;

#
# for port in range(0,1000):
#     result = scanhosts(remoteServerIP, port)
#     if result == True:
#         print("Port ",port, " is Open")
#     else:
#         print("Port ",port, "is not Open")


scanhosts()


endTime = datetime.now()

totalTime = endTime - startTime

print("Scan Completed. Total time took: ", totalTime)
