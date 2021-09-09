"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730408275"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


print("Your fortune cookie says...")
result: int = randint(1, 50)

if result > 25:
    print("Soon life will become more interesting.")
else:
    if result >= 15:
        print("You will fall in love soon.")
    else:
        if result >= 5:
            print("Your life will be happy and peaceful.")
        else:
            print("A beautiful, smart, and loving person will be coming into your life.")

print("Now, go spread positive vibes!")