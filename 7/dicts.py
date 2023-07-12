user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for key, value in user_0.items():
    print(f'{key}:{value}')
for name in sorted(user_0.keys()):
    print(name.title())
for name in sorted(user_0.values()):
    print(name)
languages: set = {'C', 'B', 'A', 'C'}
print(sorted(languages))
