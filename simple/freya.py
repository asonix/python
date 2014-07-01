#!/usr/bin/env python3

from time import sleep
from urllib.request import urlopen

url="http://isfreyareleasedyet.com"
request = urlopen(url).read().decode("utf-8")

lines = request.split("\n")

for i in lines:
    if "bug-count" in i:
        temp = i[i.find("bug-count"):]
        print("${color4}"+temp[temp.find(">")+1:temp.find("</span>")]+" Issues ${color1}until ${color3}"+temp[temp.find("until")+6:temp.find(".")])

