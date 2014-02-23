#!/usr/bin/python

import subprocess

class ColorsObj(object):
    def __init__(self, choose):
	#creates list of colors to choose from
        colors = ["#2d2d2d", "#dedede", "#f9f9f9", "#aaaaaa",
                  "#d64937", "#cc9797", "#a2dae9", "#97cc9c",
                  "#777777", "#a2c1de", "#97b2cc", "#b6a2de",
                  "#a897cc", "#bfcfde", "#adbdcc", "#c7c7c7",
                  "#cccccc", "#333333", "#999999", "#8ebfcc",
		  "#929eb0", "#a6a6a6", "#000000", "#00ff00",
		  "#ff0000"]
	
	#Indecies of colors[] for i3
        i3Light = [4, 4, 0, 4, 1, 1, 0, 1, 1, 1, 0, 1, 4, 1, 2, 1, 1, 0, 1, 4, 4, 1, 4, 1, 4, 1, 1, 17, 4, 1, 17]
        i3Dark = [4, 4, 1, 4, 0, 0, 1, 0, 0, 0, 1, 0, 4, 0, 0, 0, 0, 1, 0, 4, 4, 1, 0, 0, 4, 0, 0, 1, 4, 0, 1]
	i3Matrix = [23, 23, 22, 23, 23, 23, 22, 23, 23, 23, 22, 23, 23, 23, 22, 23, 22, 23, 22, 23, 22, 23, 23, 22, 23, 23, 22, 23, 23, 22, 23]
	i3Hacker = [24, 24, 22, 24, 24, 24, 22, 24, 24, 24, 22, 24, 24, 24, 22, 24, 22, 24, 22, 24, 22, 24, 24, 22, 24, 24, 22, 24, 24, 22, 24]
	
	#Indecies of colors[] for xterm
        xtermLight = [0, 1, 0, 2, 0, 3, 0, 4, 5, 19, 7, 8, 8, 9, 10, 11, 12, 20, 14, 15, 20, 2, 3, 1]
        xtermDark = [1, 0, 1, 0, 1, 0, 3, 5, 4, 7, 6, 18, 1, 10, 9, 12, 11, 14, 13, 16, 15, 3, 2, 22]
	xtermMatrix = [23, 22, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 22]
	xtermHacker = [24, 22, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 22]
	
	#location of background images
	i3Lightbg = "/usr/share/backgrounds/16.jpg"	
	i3Darkbg = "/usr/share/backgrounds/Space.png"
	i3Matrixbg = "~/Pictures/black.png"

	#creation of variable for transparency
	self.xtermtrans = ""
	
	#creates variables to hold stored data based on input        
	self.bg = ""
        self.ischeme = []
        self.xscheme = []
        #based on input, choose what color schemes to assign ischeme, xscheme and bg
        if choose[0:1].find('l') != -1 or choose[0:1].find('L') != -1:
            self.xtermtrans = "100"
	    self.bg = i3Lightbg
            for i in xrange(len(i3Light)):
                self.ischeme.append(colors[i3Light[i]])
            for i in xrange(len(xtermLight)):
                self.xscheme.append(colors[xtermLight[i]])
        elif choose[0:1].find('m') != -1 or choose[0:1].find('M') != -1:
	    self.xtermtrans = "100"
	    self.bg = i3Matrixbg
	    for i in xrange(len(i3Matrix)):
		self.ischeme.append(colors[i3Matrix[i]])
	    for i in xrange(len(xtermMatrix)):
		self.xscheme.append(colors[xtermMatrix[i]])
	elif choose[0:1].find('h') != -1 or choose[0:1].find('H') != -1:
	    self.xtermtrans = "100"
	    self.bg = i3Matrixbg
	    for i in xrange(len(i3Hacker)):
		self.ischeme.append(colors[i3Hacker[i]])
	    for i in xrange(len(xtermHacker)):
		self.xscheme.append(colors[xtermHacker[i]])
	else:
            self.xtermtrans = "60"
	    self.bg = i3Darkbg
            for i in xrange(len(i3Dark)):
                self.ischeme.append(colors[i3Dark[i]])
            for i in xrange(len(xtermLight)):
                self.xscheme.append(colors[xtermDark[i]])
        
#open files
foi3 = open(".i3/config", "r")
foxterm = open(".Xresources", "r")
foreread = open("reread.sh", "r")

#create lists based on read files
i3 = foi3.readlines()
xterm = foxterm.readlines()
reread = foreread.readlines()

#decide is ther variable that input is stored in
decide = raw_input("Light/Dark: ")

#create new ColorsObj object called colorscheme
colorscheme = ColorsObj(decide)

#change colors in specific lines based on colorscheme.ischeme (i3 scheme)
for i in xrange(len(i3)):
    if i3[i].find("client.focused_inactive") != -1:
        i3[i-1] = "client.focused          {:s} {:s} {:s} {:s}\n".format(colorscheme.ischeme[0], colorscheme.ischeme[1], colorscheme.ischeme[2], colorscheme.ischeme[3])
        i3[i] = "client.focused_inactive {:s} {:s} {:s} {:s}\n".format(colorscheme.ischeme[4], colorscheme.ischeme[5], colorscheme.ischeme[6], colorscheme.ischeme[7])
        i3[i+1] = "client.unfocused        {:s} {:s} {:s} {:s}\n".format(colorscheme.ischeme[8], colorscheme.ischeme[9], colorscheme.ischeme[10], colorscheme.ischeme[11])
        i3[i+2] = "client.urgent           {:s} {:s} {:s} {:s}\n".format(colorscheme.ischeme[12], colorscheme.ischeme[13], colorscheme.ischeme[14], colorscheme.ischeme[15])
    elif i3[i].find("background #") != -1:
        i3[i] = "            background {:s}\n".format(colorscheme.ischeme[16])
        i3[i+1] = "            statusline {:s}\n".format(colorscheme.ischeme[17])
        i3[i+2] = "            separator  {:s}\n".format(colorscheme.ischeme[18])
    elif i3[i].find("focused_workspace") != -1:
        i3[i] = "            focused_workspace    {:s} {:s} {:s}\n".format(colorscheme.ischeme[19], colorscheme.ischeme[20], colorscheme.ischeme[21])
        i3[i+1] = "            active_workspace     {:s} {:s} {:s}\n".format(colorscheme.ischeme[22], colorscheme.ischeme[23], colorscheme.ischeme[24])
        i3[i+2] = "            inactive_workspace   {:s} {:s} {:s}\n".format(colorscheme.ischeme[25], colorscheme.ischeme[26], colorscheme.ischeme[27])
        i3[i+3] = "            urgent_workspace     {:s} {:s} {:s}\n".format(colorscheme.ischeme[28], colorscheme.ischeme[29], colorscheme.ischeme[30])
x = 0

#change colors in every line containing the character '#' (octothorpe, pound, hashtag, whatever)
for j in xrange(len(xterm)):
        if xterm[j].find(' #') != -1:
                xterm[j] = xterm[j][:xterm[j].find('#')] + colorscheme.xscheme[x] + '\n'
                x += 1
        elif xterm[j].find(']#') != -1:
                xterm[j] = xterm[j][:xterm[j].find('[')] + '[' + colorscheme.xtermtrans + ']' + colorscheme.xscheme[x] + '\n'

#change background path in reread.sh
for k in xrange(len(reread)):
	if reread[k].find("--bg-fill") != -1:
		reread[k] = "feh --bg-fill " + colorscheme.bg + '\n'

#close opened files
foreread.close()
foi3.close()
foxterm.close()

#open all files again for writing
foreread = open("reread.sh", "wb")
foi3 = open(".i3/config", "wb")
foxterm = open(".Xresources", "wb")

#remove current text in all files
foi3.truncate()
foxterm.truncate()
foreread.truncate()

#write new text with changed colors and paths to files
foi3.writelines(i3);
foxterm.writelines(xterm);
foreread.writelines(reread);

#close files again
foi3.close()
foxterm.close()
foreread.close()

#call on reread.sh to refresh X and i3 settings
subprocess.call("~/reread.sh", shell=True)
