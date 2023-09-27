def get_formatted_name(city: str, country: str, population: int = None):
    """Строит отформатировнное название страны и города"""
    if population:
        full_name: str = f'{country} {city} {population}'.title()
    else:
        full_name: str = f'{country} {city}'.title()
    return full_name
