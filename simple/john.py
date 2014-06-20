#!/usr/bin/env python3

import json

json_file = open("absences.json")
json_data = json_file.read()
json_file.close()

data = json.loads(json_data)

totalabs = 0
for i in data:
    totalabs += int(data[i])

if totalabs < 20:
    print("What class would you like to skip? Available classes are:")
    for i in data:
        print(i)

    skpclass = input()

    if int(data[skpclass]) > 4:
        print("Don't skip that class.")
    else:
        print("It is okay to skip class, will you skip? (y/n)")
        willskp = input()
        if willskp[0].lower() == "n":
            print("Okay!")
        else:
            print("Have fun skipping!")
            data[skpclass] = str(int(data[skpclass]) + 1)
            with open("absences.json","w") as outfile:
                json.dump(data,outfile)
else:
    print("You already have "+str(totalabs)+" absences")
