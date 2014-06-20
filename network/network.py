#!/usr/bin/env python3

from subprocess import call, Popen, PIPE
import json

json_file = open("network.json")
json_data = json_file.read()
json_file.close()

data = json.loads(json_data)

ssidout = False

call(['nmcli','dev','wifi'])

while not ssidout:
    ssid = input("State desired SSID\n")
    ssidouttemp = Popen(['nmcli','dev','wifi'], stdout=PIPE).communicate()
    
    stri = ssidouttemp[0].decode("utf-8")

    if stri.find(ssid) != -1:
        ssidout = True
    
    if ssidout == False:
        check = input("SSID not present, continue? (y/n) ")
        if check.lower() == "y":
            ssidout = True

found = False
pswd = ""

output = 1

while output != 0:
    for i in data:
        if ssid == i:
            found = True
            pswd = data[i]
            a = input("Is %s the correct password? (y/n) " % pswd)
            if a.lower() != "y":
                found = False

    if found == False:
        pswd = input("What is the network password\n")
        data[ssid] = pswd

    output = call(['nmcli','dev','wifi','connect',ssid,'password',pswd,'name','wifi'])

    if output == 0 and found == False:
        with open("network.json","w") as outfile:
            json.dump(data,outfile)
    elif output != 0:
        print("Incorrect password")
