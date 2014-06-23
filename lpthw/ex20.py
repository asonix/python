#!/usr/bin/env python3

# import argv for commandline arguments
from sys import argv

# assume two arguments, store in variables
script, input_file = argv

# function to print file
def print_all(f):
    print(f.read())

# function to start from top of file
def rewind(f):
    f.seek(0)

# function to print one specified line of file
def print_a_line(line_count, f):
    print(line_count, f.readline())

# open file, store as file object
current_file = open(input_file)

print("First let's print the whole file:\n")
# calls print_all function
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
# calls rewind function
rewind(current_file)

print("Let's print three lines:")

# create variable for storing current line
current_line = 1
# call print_a_line function
print_a_line(current_line, current_file) # current_line = 1

# change current line
current_line += 1
# call print_a_line function
print_a_line(current_line, current_file) # current_line = 2

# change current line
current_line += 1
# call print_a_line function
print_a_line(current_line, current_file) # current_line = 3

