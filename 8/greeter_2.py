def get_formatted_name(first_name: str,
                       last_name: str,
                       middle_name: str = ''
                       ):
    if middle_name:
        full_name: str = f'{first_name} ' \
                         f'{last_name} ' \
                         f'{middle_name}'
    else:
        full_name: str = f'{first_name} ' \
                         f'{last_name}'
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    f_name: str = input("First name: ")
    if not f_name:
        break
    l_name: str = input("Last name: ")
    if not l_name:
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f'\nHello, {formatted_name}')
