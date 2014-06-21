#!/usr/bin/env python3

from sys import argv

script, filename = argv

input("""We're going to erase %r.
If you don't want that, hit CTRL-C (^C).
If you do want that, hit RETURN
?""" % (filename))

print("Opening the file...")
target = open(filename,"w")

print("truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

fileout = line1 + "\n" + line2 + "\n" + line3 + "\n"

print("I'm going to write these to the file.")

target.write(fileout)

print("And finally, we close it.")
target.close()
