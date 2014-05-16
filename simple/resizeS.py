#!/usr/bin/env python3
from subprocess import call

filei3 = open('.i3/config','r')
i3 = filei3.readlines()
filei3.close()

test = False

for i in range(len(i3)):
    if i3[i].find('inset') != -1:
        i3[i] = i3[i].split(" ")
        for j in range(len(i3[i])):
            if i3[i][j] != "new_window" and i3[i][j] != "inset":
                if int(i3[i][j]) > 0:
                    i3[i][j] = int(i3[i][j])-5
                    test = True
                if i3[i][j] < 0:
                    i3[i][j] = 0
                if type(i3[i][j]) != "string":
                    i3[i][j] = str(i3[i][j])
                i3[i] = " ".join(i3[i]) + "\n"
                print(i3[i])

if test == True:
    filei3 = open('.i3/config','w')
    filei3.writelines(i3)
    filei3.close()

    call(['i3-msg','restart'])
