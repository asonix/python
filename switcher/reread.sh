#!/bin/bash

i3-msg restart
xrdb ~/.Xresources

gsettings set org.gnome.desktop.background draw-background true
gsettings set org.gnome.desktop.background picture-options "spanned"
sleep 1
gsettings set org.gnome.desktop.background picture-options "zoom"
gsettings set org.gnome.desktop.background picture-uri "file:////home/riley/Pictures/wallpapers/blueandorange.png"

