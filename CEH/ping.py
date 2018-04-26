#!/usr/bin/env/ python
from platform   import system as system_name  # Returns the system/OS name
from subprocess import call   as system_call  # Execute a shell command
from datetime import datetime



def pingpy(host):
    if system_name().lower() == "windows":
        print("pinging host: ", host)
        system_call("ping -n 1 > nul", host)

    else:
        print("pinging host: ", host)
        system_call("ping -c 4 > nul", host)