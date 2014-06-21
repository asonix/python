#!/usr/bin/env python3

# imports commandline arguments from system module
from sys import argv

# assumes two arguments, assigns first to script, second to filename
script, filename = argv

# opens file object from cmd args, stores in txt
txt = open(filename)

# prints line of text with name of file
print("Here's your file %r:" % (filename))
# prints contents of file
print(txt.read())

# closes file
txt.close()
