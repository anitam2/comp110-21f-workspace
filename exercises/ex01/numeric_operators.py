"""Program that performs computations on input numbers using special numeric operators."""

__author__ = "730408275"

x: str = input("Left-hand side: ")
int_x = int(x)
y: str = input("Right-hand side: ") 
int_y = int(y)

print(x + " ** " + y + " is " + str(int_x ** int_y))
print(x + " / " + y + " is " + str(int_x / int_y))
print(x + " // " + y + " is " + str(int_x // int_y))
print(x + " % " + y + " is " + str(int_x % int_y))