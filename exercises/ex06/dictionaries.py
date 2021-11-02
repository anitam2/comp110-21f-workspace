"""Practice with dictionaries."""

__author__ = "730408275"

# Define your functions below


def invert(given_dict: dict[str, str]) -> dict[str, str]:
    """Given a dictionary of [str, str], invert should return a dict[str, str] that inverts the keys and the values. The keys of the input list becomes the values of the output list and vice versa."""
    result: dict[str, str] = {}
    for key in given_dict:
        if key in result:
            raise KeyError("KeyError")
        else:
            result[given_dict[key]] = key
    return result


def favorite_color(given_dict: dict[str, str]) -> str:
    """Has one parameter, of type dict[str, str] of names and favorite colors. It returns a str which is the color that appears most frequently. If there is a tie for most popular color, return the color that appeared in the dictionary first."""
    count_dict: dict[str, int] = {}
    fav_color: str = ""
    max_count: int = 0
    for key in given_dict:
        if given_dict[key] in count_dict:
            count_dict[given_dict[key]] += 1
        else:
            count_dict[given_dict[key]] = 1
    
    for key in count_dict:
        if count_dict[key] > max_count:
            max_count = count_dict[key]
            fav_color = key
        if count_dict[key] == max_count:
            max_count = count_dict[key]
            fav_color = key
    return fav_color


def count(given_list: list[str]) -> dict[str, int]:
    """Given a list[str], this function will produce a dict[str, int] where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}

    i: int = 1
    while i < len(given_list):
        if given_list[i] in result:
            result[given_list[i]] += 1
        else:
            result[given_list[i]] = 1
        i += 1

    return result

print(count(["hi", "hi", "bye"]))