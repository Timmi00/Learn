class Restaurant:
    """простая модель ресторана"""

    def __init__(self, restaurant_name: str, cuisine_type: str):
        """Иннициализация атрибутов"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self, number: int):
        self.number_served = number

    def read_number_served(self):
        print(f'Колличество обслуженных посетителей: {self.number_served}')

    def increment_number_served(self, count: int):
        self.number_served += count

    def describe_restaurant(self):
        """Создание метода"""
        print(f'Ресторан {self.restaurant_name} подает блюда {self.cuisine_type}')

    def open_restaurant(self):
        print(f'Ресторан {self.restaurant_name} открыт для посетителей')
