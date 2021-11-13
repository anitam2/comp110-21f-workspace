"""An exercise in remainders and boolean logic."""

__author__ = "730408275"


integer = int(input("Enter an int: "))

if (integer % 2 == 0) and (integer % 7 == 0):
    print("TAR HEELS")
elif integer % 2 == 0:
    print("TAR")
elif integer % 7 == 0:
    print("HEELS")
else:
    print("CAROLINA")