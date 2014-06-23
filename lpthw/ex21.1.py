#!/usr/bin/env python3

def add(a, b):
    return 2*a + b

def subtract(a, b):
    return 5 * (a - b)

def multiply(a, b):
    return a * b * (a / b)

def divide(a, b):
    return a * b / 5

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(age, height, weight, iq)
