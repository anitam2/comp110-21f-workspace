"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730408275"


def test_invert() -> None:
    """Tests invert with normal test case."""
    given_dict: dict[str, str] = {'anita': 'murali', 'uma': 'rajaratnam'}
    assert invert(given_dict) == {'murali': 'anita', 'rajaratnam': 'uma'}


def test_invert_again() -> None:
    """Tests invert again with normal test case."""
    given_dict: dict[str, str] = {'dog': 'cat', 'mouse': 'horse', 'pig': 'turtle'}
    assert invert(given_dict) == {'cat': 'dog', 'horse': 'mouse', 'turtle': 'pig'}


def test_invert_empty() -> None:
    """Tests invert with empty dict."""
    given_dict: dict[str, str] = {}
    assert invert(given_dict) == {}


def test_favorite_color() -> None:
    """Tests favorite color with normal test case."""
    given_dict: dict[str, str] = {'anita': 'red', 'jasper': 'pink', 'peter': 'red'}
    assert favorite_color(given_dict) == "red"


def test_favorite_color_again() -> None:
    """Tests favorite color with normal test case."""
    given_dict: dict[str, str] = {'anita': 'red'}
    assert favorite_color(given_dict) == "red"


def test_favorite_color_tie() -> None:
    """Tests favorite color with a tie for most popular color."""
    given_dict: dict[str, str] = {'anita': 'red', 'jasper': 'red'}
    assert favorite_color(given_dict) == "red"
 

def test_count() -> None:
    """Tests count with normal test case."""
    given_list: list[str] = ['murali', 'murali']
    assert count(given_dict) == {'murali': 2}


def test_count_again() -> None:
    """Tests count with normal test case."""
    given_list: list[str] = ['COMP', 'COMP', 'MATH']
    assert count(given_dict) == {'COMP': 2, 'MATH': 1}


def test_count_empty() -> None:
    """Tests count with empty list."""
    given_list: list[str] = []
    assert count(given_dict) == {}