"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730408275"


class Simpy:
    """Simpy class."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Initalize a new Simpy object."""
        self.values = values
    
    def __str__(self) -> str:
        """Str representation of a Simpy object."""
        return f"Simpy({self.values})"

    def fill(self, value: float, times: int) -> None:
        """Fill values array by mutating object called on."""
        # Start with empty values list
        self.values = []
        i: int = 0
        while i < times:
            self.values.append(value)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in a range of values."""
        self.values = []
        assert step != 0.0    # making sure step is not 0
        if step > 0.0:
            next_value: float = start
            while next_value < stop:
                self.values.append(next_value)
                next_value += step
        else:
            next_value: float = start
            while next_value > stop:
                self.values.append(next_value)
                next_value += step

    def sum(self) -> float:
        """Delegate this algorithm to the built-in sm function."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload for addition."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overload for exponentiation."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Operator overload for ==."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for values in self.values:
                if values == rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            i: int = 0
            while i < len(self.values):
                assert len(self.values) == len(rhs.values)
                if rhs.values[i] == self.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Operator overload for greater than."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for values in self.values:
                if values > rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            i: int = 0
            while i < len(self.values):
                assert len(self.values) == len(rhs.values)
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Subscription operator with Simpy objects."""
        result: Simpy = Simpy([])
        if isinstance(rhs, int):
            return self.values[rhs]
        i: int = 0
        while i < len(self.values):
            if rhs[i]:
                result.values.append(self.values[i]) 
            i += 1 
        return result