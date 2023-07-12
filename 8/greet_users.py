def greet_users(names: list):
    """Вывод простого приветствия для каждого пользователя в списке"""
    for name in names:
        msg: str = f"Hello, {name.title()} "
        if name == 'Bella':
            msg += 'CHAO'
        print(msg)


usernames: list = ['hannah', 'Bella', 'Archi']
greet_users(usernames)
