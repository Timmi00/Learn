class Restaurant:
    """простая модель ресторана"""

    def __init__(self,restaurant_name: str, cuisine_type: str):
        """Иннициализация атрибутов"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Создание метода"""
        print(f'Ресторан {self.restaurant_name} подает блюда {self.cuisine_type}')

    def open_restaurant(self):
        print(f'Ресторан {self.restaurant_name} открыт для посетителей')


restaurant_blr = Restaurant('Вежа', 'Белорусской кухни')
print(restaurant_blr.restaurant_name)
print(restaurant_blr.cuisine_type)
restaurant_blr.describe_restaurant()
restaurant_blr.open_restaurant()
restaurant_mex = Restaurant('MeXico', 'Мексиканской кухни')
restaurant_pl = Restaurant('Pane', 'Польской кухни')
restaurant_pl.open_restaurant()
restaurant_pl.describe_restaurant()
restaurant_mex.open_restaurant()
restaurant_mex.describe_restaurant()

