#!/usr/bin/env python3
from os import remove
from shutil import copyfile
from subprocess import call

def switch(dest):
    remove('.xinitrc')
    copyfile('.xinitrc'+dest,'.xinitrc')

done = False
while done == False:
    wm = input("What WM or DE would you like to use?\n\nOptions:\n>BSPWM\n>Gnome\n>Herbstluftwm\n>i3\n>Pantheon\n\n")
    done = True
    
    if wm[0].lower() == 'b':
        switch('bspwm')
    elif wm[0].lower() == 'p':
        switch('pantheon')
    elif wm[0].lower() == 'i':
        switch('i3')
    elif wm[0].lower() == 'g':
        switch('gnome')
    elif wm[0].lower() == 'h':
        switch('herbstluftwm')
    else:
        done = False
call(['pkill','x'])
call(['startx'])
