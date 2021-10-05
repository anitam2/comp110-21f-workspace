"""List utility functions."""

<<<<<<< HEAD
__author__ = "730408275"


def all(xs: list[int], a: int) -> bool:
    """Given a list of ints and an int, all returns a bool indicating whether or not all the ints in the list are the same as the given int."""
    i: int = 0
    if len(xs) == 0:
        return False
    while i < len(xs):
        if xs[i] != a:
            return False
        i += 1
    return True


def is_equal(xs: list[int], ab: list[int]) -> bool:
    """Given two lists of int values, is_equal returns True if every element at every index is equal in both lists."""
    i: int = 0
    if len(xs) != len(ab):
        return False
    else:
        while i < len(xs):
            if xs[i] != ab[i]:
                return False
            i += 1
        return True


def max(input: list[int]) -> int:
    """The max function is given a list of ints and returns the largest in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    current_max: int = input[0]
    i: int = 1
    while i < len(input):
        if input[i] > current_max:
            current_max = input[i]
        i += 1
    return current_max
=======
__author__ = "123456789"


# TODO: Implement your functions here.
>>>>>>> 75d5a25d0b84063cbf6a8cc58cc71c34269e73d8
