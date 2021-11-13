"""Drawing forests in a loop."""

__author__ = "730408275"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

depth = int(input("Depth: "))
i: int = 0
image: str = ""

while i < depth: 
    image = image + TREE
    print(image)
    i = i + 1