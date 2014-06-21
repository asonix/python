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

# prints line of text asking for input
print("Type the filename again:")
# stores input (assumed filename) in file_again
file_again = input("> ")

# stores file_again as file object in txt_again
txt_again = open(file_again)

# prints contents of file
print(txt_again.read())

# closes file
txt_again.close()
