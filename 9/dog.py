class Dog:
    """Простая модель собаки"""

    def __init__(self, name: str, age: int):
        """Иннициализация атрибутов"""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садится по команде"""
        print(f'{self.name} is now sitting')

    def roll_over(self):
        """Собака перекавтывается по комманде"""
        print(f'{self.name} rolled over')


my_dog = Dog('Willie', 6)
print(f'My dog\'s name is {my_dog.name}')
print(f'My dog is {my_dog.age} years old')
