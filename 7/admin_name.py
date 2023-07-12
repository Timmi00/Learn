user_names: list = [
    'Andy', 'Harry', 'ADmin', 'vero', 'hulio', 'gOMon'
]
new_users: list = [
    '1', '2', 'vero', '4', 'Gomon'
]
user_names_tittle: list = [
    i.title() for i in user_names
]
if new_users:
    for new_user in new_users:
        if new_user.title() in user_names_tittle:
            print(
                f'Hello {new_user.title()}, would you like to see a status report?'
            )
        else:
            print(
                f'Hello {new_user.title()}, thank you for logging in again»'
            )
else:
    print(
        'We need to ind some users!'
    )
