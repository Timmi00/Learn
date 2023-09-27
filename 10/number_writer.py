import json


numbers: list = [2, 3, 5, 7, 11, 13]

filename: str = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
