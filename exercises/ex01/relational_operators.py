"""Program that compares input numbers using relational operators."""

__author__ = "730408275"

x: str = input("Left-hand side: ")
int_x = int(x)
y: str = input("Right-hand side: ")
int_y = int(y)

print(x + " < " + y + " is " + str(x < y))
print(x + " >= " + y + " is " + str(x >= y))
print(x + " == " + y + " is " + str(x == y))
print(x + " != " + y + " is " + str(x != y))