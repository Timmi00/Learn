import json

filename: str = 'username.json'
try:
    with open(filename) as f:
        username: str = json.load(f)
except FileNotFoundError:
    username: str = input('введите свое имя: ')
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f'We remember you when you comeback, {username}!')
else:
    print(f'Welcome back {username}!')

