"""
This module contains functions for performing mathematical operations.

Functions:
    add -- adds two numbers
    subtract -- subtracts two numbers
    multiply -- multiplies two numbers
    divide -- divides two numbers
"""
import pandas as pd

def add(val_one: int, val_two: int):
    """Sums args

    Args:
        x (int): arg1
        y (int): arg2

    Returns:
        int: sum of args
    """
    if not isinstance(val_one, int) or not isinstance(val_two, int):
        raise TypeError("Both arguments must be integers")
    return val_one + val_two

print(add("1234", "1234"))

STRING: str = 'test,test'
INTEGER: int = 123
FLOAT: float = 123,54

DATA = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}

DF: pd.DataFrame = pd.DataFrame(DATA)
