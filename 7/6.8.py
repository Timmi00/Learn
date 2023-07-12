pets: list[dict] = [
    {'Alice': {'vid': 'sobaka', 'name': 'tim'}},
    {'John': {'vid': 'cat', 'name': 'Hom'}},
]
for names in pets:
    for name, value in names.items():
        print(f'Kli4ka: {name}. ')
        for i, n in value.items():
            print(f'{i}: {n}')
places: dict = {
    'andy': ['minsk', 'suinsk'],
    'bandy': ['popa', 'dupa', 'copa'],
    'vandy': [],
    'sandy': ['ribinsk']
}
for name, place in places.items():
    if place:
        print(f'\n{name}')
        for plac in place:
            print(plac)
