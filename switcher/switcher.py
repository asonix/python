#!/usr/bin/env python3
from subprocess import call

#creates list of colors to choose from
colors = ["#2d2d2d","#dedede","#f9f9f9","#aaaaaa",
          "#d64937","#c09853","#b94a48","#f9f9f9",
          "#777777","#859d00","#3a87ad","#ad3ac8",
          "#a897cc","#a0b0de","#268bd2","#c7c7c7",
          "#cccccc","#333333","#f57900","#577382",
          "#929eb0","#a6a6a6","#000000","#00ff00",
          "#ff0000","#555555","#24507c","#e5e5e5"]

def determine_hex(value):
    allowed = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    value = value[1:]
    for i in value:
        if i not in allowed:
            return(False)
    return(True)

def find_and_replace_hex(document,values,iterator):
    for i in range(len(document)):
        if document[i].find('#') != -1:
            if determine_hex(document[i][document[i].find('#'):document[i].find('#')+7]):
                index = document[i].find('#')
                begin = document[i][:index]
                rec_doc = [document[i][index+7:]]
                temp = begin + values[iterator]
                result = find_and_replace_hex(rec_doc,values,iterator+1)
                document[i] = temp + str(result[0][0])
                iterator = result[1]
    return([document,iterator])

class WmObj(object):
    def __init__(self,choose):
        i3Light =  [ 4, 4, 0, 4, 1,25, 0, 1, 1,25, 0, 1, 4, 1, 2, 1, 1, 0, 1, 4, 4, 1, 4, 1, 4, 1, 1,17, 4, 1,17]
        i3Dark =   [ 4, 4, 1, 4, 0,25, 1, 0, 0,25, 1, 0, 4, 0, 0, 0, 0, 1, 0, 0, 0, 4, 0, 0, 4, 0, 0, 1, 4, 0, 1]
        i3Matrix = [23,23,22,23,23,23,22,23,23,23,22,23,23,23,22,23,22,23,22,23,22,23,23,22,23,23,22,23,23,22,23]
        i3Hacker = [24,24,22,24,24,24,22,24,24,24,22,24,24,24,22,24,22,24,22,24,22,24,24,22,24,24,22,24,24,22,24]
        
        backgrounds = [ "/home/riley/Pictures/wallpapers/flora.png",
                        "/home/riley/Pictures/wallpapers/floratree.png",
                        "/home/riley/Pictures/wallpapers/katia_managan.jpg",
                        "/home/riley/Pictures/wallpapers/quill_weave.jpg",
                        "/home/riley/Pictures/wallpapers/dragons.png",
                        "/home/riley/Pictures/wallpapers/sunhorse.jpg",
                        "/home/riley/Pictures/wallpapers/princesshorses.jpg",
                        "/home/riley/Pictures/wallpapers/sunandmountain.jpg",
                        "/home/riley/Pictures/wallpapers/xp.png",
                        "/home/riley/Pictures/wallpapers/circularWmill.png",
                        "/home/riley/Pictures/wallpapers/blueandorange.png",
                        "/home/riley/Pictures/wallpapers/lightgem.png",
                        "/home/riley/Pictures/wallpapers/Lighthouse.jpg",
                        "/home/riley/Pictures/wallpapers/flutter.jpg",
                        "/home/riley/Pictures/wallpapers/rainbow.jpg",
                        "/home/riley/Pictures/wallpapers/phoenix.jpg",
                        "/home/riley/Pictures/wallpapers/moonhorse.jpg",
                        "/home/riley/Pictures/wallpapers/frogadier.png",
                        "/home/riley/Pictures/wallpapers/black.png"]

        bgnum = int(input("What background would you like (1/2/3/4...)?\n\
  1. Flora Ocean\n\
  2. Flora Tree\n\
  3. Katia Managan\n\
  4. Quil Weave\n\
  5. Dragons\n\
  6. Celestia\n\
  7. Princesses\n\
  8. Low Poly Mountain\n\
  9. XP\n\
 10. Wmill Circular\n\
 11. Blue and Orange\n\
 12. Light Gem\n\
 13. Light House\n\
 14. Flutter\n\
 15. Rainbow\n\
 16. Phoenix\n\
 17. Luna\n\
 18. Frogadier\n\
 19. Black\n\
 \n"))
        if (bgnum <= len(backgrounds)):
            self.bg = backgrounds[bgnum-1]
        else:
            self.bg = backgrounds[len(backgrounds)-1]

        self.ischeme = []
        self.tempi = []

        if choose[0].lower() == 'l':
            self.tempi = i3Light
        elif choose[0].lower() == 'm':
            self.tempi = i3Matrix
        elif choose[0].lower() == 'h':
            self.tempi = i3Hacker
        elif choose[0].lower() == 'd':
            self.tempi = i3Dark
            
        for i in range(len(self.tempi)):
            self.ischeme.append(colors[self.tempi[i]])

class TermObj(object):
    def __init__(self,choose):
        termTrans =  [ 7, 1, 7, 1, 7, 1, 3, 5, 6, 7, 4,18, 3,10, 9,12,11,14,13,16,15, 3, 3, 1]
        termLight =  [ 0,27, 0, 1, 0, 1, 3, 5, 6, 7, 4,18, 3,10, 9,12,11,14,13,16,15, 3, 0,27]
        termDark =   [ 1, 0, 1, 0, 1, 0, 3, 5, 6, 7, 4,18, 3,10, 9,12,11,14,13,16,15, 3, 2, 0]
        termMatrix = [23,22,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,22]
        termHacker = [24,22,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,22]

        self.alternating = "bindsym $mod+Return exec urxvt\n"
        self.trans = ""
        self.tscheme = []
        self.tempt = []
        self.fading = 0

        if choose[0].lower() == 'l':
            self.trans = "100"
            self.tempt = termLight
        elif choose[0].lower() == 'm':
            self.trans = "100"
            self.tempt = termMatrix
        elif choose[0].lower() == 'h':
            self.trans = "100"
            self.tempt = termHacker
        elif choose[0].lower() == 'd':
            self.trans = "100"
            self.tempt = termDark
        elif choose[0].lower() == 't':
            self.trans = "0"
            self.tempt = termTrans
            self.fading = 5
        elif choose[0].lower() == 'a':
            self.trans = "0"
            self.tempt = termTrans
            self.fading = 0
            self.alternating = "bindsym $mod+Return exec ./altTheme.py && urxvt\n"
        
        for i in range(len(self.tempt)):
            self.tscheme.append(colors[self.tempt[i]])

wmdecide = input('What WM theme would you like to use?\n\
\n\
Options:\n\
>Light Numix\n\
>Dark Numix\n\
>Hacker\n\
>Matrix\n\
\n')
i3colors = WmObj(wmdecide)

termdecide = input('What terminal theme would you like to use?\n\
\n\
Options:\n\
>Light Numix\n\
>Dark Numix\n\
>Alternating Numix\n\
>Hacker\n\
>Matrix\n\
>Transparent\n\
\n')
termcolors = TermObj(termdecide)

fi3 = open('.i3/config','r')
fterm = open('.Xresources','r')
freread = open('.reread.sh','r')

i3 = fi3.readlines()
term = fterm.readlines()
reread = freread.readlines()

fi3.close()
fterm.close()
freread.close()

i3 = find_and_replace_hex(i3,i3colors.ischeme,0)[0]
term = find_and_replace_hex(term,termcolors.tscheme,0)[0]

for i in range(len(i3)):
    if i3[i].find('$mod+Return') != -1:
        i3[i] = termcolors.alternating

for i in range(len(term)):
    if term[i].find('fading') != -1:
        term[i] = term[i].split(' ')
        for j in range(len(term[i])):
            if term[i][j] != "*fading:" and term[i][j] != "\n":
                term[i][j] = str(termcolors.fading)
        if type(term[i]) != "string":
            term[i] = ' '.join(term[i])+'\n'

for i in range(len(term)):
    if term[i].find(']#') != -1:
        term[i] = term[i][:term[i].find('[')]+'['+termcolors.trans+term[i][term[i].find(']'):]

for j in range(len(reread)):
    if reread[j].find('picture-uri') != -1:
        reread[j] = 'gsettings set org.gnome.desktop.background picture-uri "file:///'+i3colors.bg+'"\n'

fi3 = open('.i3/config','w')
fterm = open('.Xresources','w')
freread = open('.reread.sh','w')

fi3.truncate()
fterm.truncate()
freread.truncate()

fi3.writelines(i3)
fterm.writelines(term)
freread.writelines(reread)

fi3.close()
fterm.close()
freread.close()

call('./.reread.sh',shell=True)
