#!/usr/bin/env python3

# defines a function with two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # prints number of cheeses and crackers with some useless info
    print("You have %d cheeses!" % (cheese_count))
    print("You have %d boxes of crackers!" % (boxes_of_crackers))
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
# calls function with 20 and 30 as arguments
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# calls function with 10 and 50 as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too")
# calls function with 30 and 11 as arguments
cheese_and_crackers(10+20, 5+6)

print("And we can combine the two, variables and math")
# calls function with 110 and 1050 as arguments
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
