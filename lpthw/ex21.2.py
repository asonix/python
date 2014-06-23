#!/usr/bin/env python3

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# 9*17/2+(5*7-3)
# 108.5

print(add(divide(multiply(9, 17), 2), subtract(multiply(5, 7), 3)))

