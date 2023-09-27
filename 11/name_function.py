def get_formatted_name(first: str, last: str, middle: str = ''):
    """Строит отформатировнное полное имя"""
    if middle:
        full_name: str = f'{first} {middle} {last}'.title()
    else:
        full_name: str = f'{first} {last}'.title()
    return full_name

