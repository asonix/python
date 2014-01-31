#!/usr/bin/python

import subprocess

class Numix(object):
    def __init__(self, choose):
        colors = ["2d2d2d", "dedede", "f9f9f9", "aaaaaa",
                  "d64937", "cc9797", "a2dae9", "97cc9c",
                  "777777", "a2c1de", "97b2cc", "b6a2de",
                  "a897cc", "bfcfde", "adbdcc", "c7c7c7",
                  "cccccc", "333333", "999999"]
        i3Light = [4, 4, 0, 4, 1, 1, 0, 1, 1, 1, 0, 1, 4, 1, 2, 1, 1, 0, 1, 17, 4, 1, 17, 1, 1, 0, 1, 17, 4, 1, 17]
        i3Dark = [4, 4, 1, 4, 0, 0, 1, 0, 0, 0, 1, 0, 4, 0, 0, 0, 0, 1, 0, 4, 4, 1, 0, 0, 1, 0, 0, 1, 4, 0, 1]
        xtermLight = [0, 1, 0, 2, 0, 3, 0, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15, 16, 2, 3]
        xtermDark = [1, 0, 1, 0, 1, 0, 3, 5, 4, 7, 6, 18, 1, 10, 9, 12, 11, 14, 13, 16, 15, 3, 2]
        
        self.ischeme = []
        self.xscheme = []
        
        if choose[0:1].find('l') != -1 or choose[0:1].find('L') != -1:
            for i in xrange(len(i3Light)):
                self.ischeme.append(colors[i3Light[i]])
            for i in xrange(len(xtermLight)):
                self.xscheme.append(colors[xtermLight[i]])
        else:
            for i in xrange(len(i3Dark)):
                self.ischeme.append(colors[i3Dark[i]])
            for i in xrange(len(xtermLight)):
                self.xscheme.append(colors[xtermDark[i]])
        

foi3 = open(".i3/config", "r")
foxterm = open(".Xresources", "r")

i3 = foi3.readlines()
xterm = foxterm.readlines()

decide = raw_input("Light/Dark: ")

colorscheme = Numix(decide)

for i in xrange(len(i3)):
    if i3[i].find("client.focused_inactive") != -1:
        i3[i-1] = "client.focused          #{:s} #{:s} #{:s} #{:s}\n".format(colorscheme.ischeme[0], colorscheme.ischeme[1], colorscheme.ischeme[2], colorscheme.ischeme[3])
        i3[i] = "client.focused_inactive #{:s} #{:s} #{:s} #{:s}\n".format(colorscheme.ischeme[4], colorscheme.ischeme[5], colorscheme.ischeme[6], colorscheme.ischeme[7])
        i3[i+1] = "client.unfocused        #{:s} #{:s} #{:s} #{:s}\n".format(colorscheme.ischeme[8], colorscheme.ischeme[9], colorscheme.ischeme[10], colorscheme.ischeme[11])
        i3[i+2] = "client.urgent           #{:s} #{:s} #{:s} #{:s}\n".format(colorscheme.ischeme[12], colorscheme.ischeme[13], colorscheme.ischeme[14], colorscheme.ischeme[15])
    elif i3[i].find("background #") != -1:
        i3[i] = "            background #{:s}\n".format(colorscheme.ischeme[16])
        i3[i+1] = "            statusline #{:s}\n".format(colorscheme.ischeme[17])
        i3[i+2] = "            separator  #{:s}\n".format(colorscheme.ischeme[18])
    elif i3[i].find("focused_workspace") != -1:
        i3[i] = "                focused_workspace     #{:s} #{:s} #{:s}\n".format(colorscheme.ischeme[19], colorscheme.ischeme[20], colorscheme.ischeme[21])
        i3[i+1] = "                active_workspace     #{:s} #{:s} #{:s}\n".format(colorscheme.ischeme[22], colorscheme.ischeme[23], colorscheme.ischeme[24])
        i3[i+2] = "                inactive_workspace   #{:s} #{:s} #{:s}\n".format(colorscheme.ischeme[25], colorscheme.ischeme[26], colorscheme.ischeme[27])
        i3[i+3] = "                urgent_workspace     #{:s} #{:s} #{:s}\n".format(colorscheme.ischeme[28], colorscheme.ischeme[29], colorscheme.ischeme[30])
x = 0
for j in xrange(len(xterm)):
        if xterm[j].find('#') != -1:
                xterm[j] = xterm[j][:xterm[j].find('#')+1] + colorscheme.xscheme[x] + '\n'
                x += 1

foi3.close()
foxterm.close()

foi3 = open(".i3/config", "wb")
foxterm = open(".Xresources", "wb")

foi3.truncate()
foxterm.truncate()

foi3.writelines(i3);
foxterm.writelines(xterm);

foi3.close()
foxterm.close()

subprocess.call("~/logout.sh", shell=True)
