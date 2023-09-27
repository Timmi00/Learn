import json


filename: str = 'numbers.json'

with open(filename) as f:
    numbers: list = json.load(f)

print(numbers)
