#!/usr/bin/env python3

def while_test(max):
    """return list of digits from 0 until max"""
    i = 0
    numbers = []

    while i < max:
        print("At the  top i is %d" % (i))
        numbers.append(i)

        i = i + 1
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % (i))

    return numbers

numbers = while_test(9)
print("The numbers: ")

for num in numbers:
    print(num)
