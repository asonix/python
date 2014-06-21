#!/usr/bin/env python3

from sys import argv

script, filename = argv

print("Opening %r" % (filename))
target = open(filename)

print("The file's contents are:\n")
print(target.read())
print("Closing...")
target.close()
