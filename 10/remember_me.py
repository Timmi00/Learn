import json


def get_stored_username():
    """Получает хранимое имя, если оно существует"""
    filename: str = 'username.json'
    try:
        with open(filename) as f:
            username: str = json.load(f)
    except FileNotFoundError:
        return None
    else:
        answer: str = input(f'Your name is {username} ?')
        if answer == 'yes':
            return username
        else:
            return None


def get_new_user():
    """Запрашивает новое имя пользователя."""
    username: str = input('What is your name')
    filename: str = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Приветствует пользователя по имени"""
    username: str = get_stored_username()
    if username:
        print(f'Welcome back {username}!')
    else:
        username: str = get_new_user()
        print(f'We remember you when you come back, {username}!')


greet_user()
