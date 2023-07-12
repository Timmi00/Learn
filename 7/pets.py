pets: list = [
    'cat',
    'dog',
    'cat',
    'goldfish',
    'rabbit',
    'cat',
]
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
