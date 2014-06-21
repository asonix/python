#!/usr/bin/env python3

# prints line of text asking for input
print("Type the filename:")
# stores input (assumed filename) in filename
filename = input("> ")

# stores filename as file object in txt
txt = open(filename)

# prints contents of file
print(txt.read())

# closes file
txt.close()
