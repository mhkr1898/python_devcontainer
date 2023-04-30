import pandas as pd

def add(val_one: int, val_two: int):
    return val_one + val_two

print(add(1234, 1234))

STRING: str = 'test,test'
INTEGER: int = 123
FLOAT: float = 123.54

DICTIONARY: dict = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}

DATAFRAME: pd.DataFrame = pd.DataFrame(DICTIONARY)
