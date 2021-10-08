"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730408275"


def test_utils_only_evens_all_odd() -> None:
    """Tests only_evens with a list with all odd integers."""
    xs: list[int] = [1, 5, 3]
    assert only_evens(xs) == []


def test_utils_only_evens_all_even() -> None:
    """Tests only_evens with a list with all even integers."""
    xs: list[int] = [6, 4, 2, 102]
    assert only_evens(xs) == [6, 4, 2, 102]


def test_utils_only_evens_empty() -> None:
    """Tests only_evens with an empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_utils_sub() -> None:
    """Tests sub with a normal list of integers."""
    xs: list[int] = [10, 20, 30, 40]
    start: int = 1
    end: int = 3
    assert sub(xs, start, end) == [20, 30]


def test_utils_sub_whole_list() -> None:
    """Tests sub with a normal list of integers, but asks for the entire start to end index."""
    xs: list[int] = [10, 20, 30, 40]
    start: int = 0
    end: int = 4
    assert sub(xs, start, end) == [10, 20, 30, 40]


def test_utils_sub_0_index() -> None:
    """Tests sub with both indexes at 0."""
    xs: list[int] = [5, -40, 40, 10]
    start: int = 0
    end: int = 0
    assert sub(xs, start, end) == []


def test_utils_concat() -> None:
    """Tests concat with a list with 2 lists of normal integers."""
    xs: list[int] = [1, 2, 3, 4]
    xs1: list[int] = [5, 6, 7, 8]
    assert concat(xs, xs1) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_utils_concat_first_list_empty() -> None:
    """Tests concat with the first list empty."""
    xs: list[int] = []
    xs1: list[int] = [-4, -5, -8]
    assert concat(xs, xs1) == [-4, -5, -8]


def test_utils_concat_again() -> None:
    """Tests concat with a normal list of integers."""
    xs: list[int] = [0, 0, -1000]
    xs1: list[int] = [4848, -9, 2]
    assert concat(xs, xs1) == [0, 0, -1000, 4848, -9, 2]