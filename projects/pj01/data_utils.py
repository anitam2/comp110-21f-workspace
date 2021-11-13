"""Utility functions."""

__author__ = "123456789"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-orientated table to a columnn-orientated table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. `dict[str, list[str]]`) table with only the first `N` (a parameter) rows of data for each column."""
    result: dict[str, list[str]] = {}
    first_row: list[str] = list(table.keys())

    for column in first_row:
        first_N_values: list[str] = []
        i: int = 0
        if N >= len(table[column]):
            return table
        else:
            while i < N:
                first_N_values.append(table[column][i])
                i += 1
            result[column] = first_N_values
    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. `dict[str, list[str]]`) table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}

    for column in names:
        result[column] = table[column]
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. `dict[str, list[str]]`) table with two column-based tables combined."""
    result: dict[str, list[str]] = {}

    for column in table1:
        result[column] = table1[column]
    for column in table2:
        if column in result:
            result[column] = table1[column] + table2[column]
        else:
            result[column] = table2[column]

    return result


def count(values: list[str]) -> dict[str, int]:
    """Given a `list[str]`, this function will produce a `dict[str, int]` where each key is a unique value in the given list and each value associated is the _count_ of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}

    for value in values:
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
    return result