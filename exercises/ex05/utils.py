"""List utility functions part 2."""

__author__ = "730408275"

# Define your functions below


def only_evens(xs: list[int]) -> list[int]:
    """Given a list of ints, only_evens returns a list containing only the elements of the input list that were even."""
    even_list: list[int] = []
    for number in xs:
        if number % 2 == 0:
            even_list.append(number)
    return even_list


def sub(xs: list[int], start: int, end: int) -> list[int]:
    """Given a list of ints, a start index, and an end index (not inclusive), sub generates a list which is a subset of the given list, between the specified start index and the end index - 1."""
    i: int = 0
    new_list: list[int] = []
    while i < len(xs):
        if i >= start and i < end:
            new_list.append(xs[i])
        i += 1
    return new_list


def concat(xs: list[int], xs1: list[int]) -> list[int]:
    """Given two Lists of ints, concat should generate a new List which contains all of the elements of the first list followed by all of the elements of the second list."""
    i: int = 0
    new_list: list[int] = []
    while i < len(xs):
        new_list.append(xs[i])
        i += 1
    j: int = 0
    while j < len(xs1):
        new_list.append(xs1[j])
        j += 1
    return new_list