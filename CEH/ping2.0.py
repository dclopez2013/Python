import ipaddress
import os
print("*" * 60)
user_input = input("Enter a internet address to sweep \n")
print("*" * 60)

network = ipaddress.ip_network((user_input))
#192.168.43.29
#216.58.216.100

for i in network.hosts():

    try:
        result =os.system('ping %s -n 1 > nul' % (i))

        if(result ==0):
            print(i," Host is up")
        else:
            print(i, " host is down")
    except os.CalledProcessError as e:
        error =e
