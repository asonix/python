#!/bin/bash

i3-msg restart
xrdb ~/.Xresources

feh --bg-fill /usr/share/backgrounds/Purple.png

nohup ./alternating_layouts.py & exit
