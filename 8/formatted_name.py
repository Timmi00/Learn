def get_formatted_name(first_name: str,
                       last_name: str,
                       middle_name: str = ''
                       ):
    if middle_name:
        full_name: str = f'{first_name} ' \
                         f'{last_name} ' \
                         f'{middle_name}'.title()
    else:
        full_name: str = f'{first_name} ' \
                         f'{last_name}'.title()
    return full_name


print(get_formatted_name('jimmy', 'hendrix'))
print(get_formatted_name('john', 'lee', 'Hooker'))
