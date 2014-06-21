#!/usr/bin/env python3

from sys import argv

j = 0
for i in argv:
    print("variable #%d is" % (j), i)
    j += 1
