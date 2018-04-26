#!/usr/bin/env python3


import subprocess as sp

from subprocess import call as system_call

from datetime import datetime

#clear the screen


#get user input

print("Enter subnet address to scan:\n")
remoteServer = input()



print("Subnet Address ip\n")

print("*" * 50)
print("scanning host now")
print("*" * 50)

newip = remoteServer.index(".",0,remoteServer.__len__())

newhost = remoteServer.count(".")
indexL = remoteServer


count = 0
pCount = 0
mylist=[]

for x in range(len(indexL)):
    if count <3:
        if indexL[x] == ".":
            if count < 3:
                count += 1
                mylist.append(indexL[x])
              #  print(count)

        elif not indexL[x] == ".":
            if count <3:
                mylist.append(indexL[x])
             #   print(count)


myip = "".join(mylist)

print(myip)

startTime = datetime.now()

print("scan started at", startTime)