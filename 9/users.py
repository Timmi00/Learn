class User:
    """Модель пользователя"""

    def __init__(self, first_name: str, last_name: str, age: int, email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print(f'\n{self.first_name}-{self.last_name}-{self.age}-{self.email}')

    def greet_user(self):
        print(f'\nHello my dear {self.first_name} {self.last_name}')


tim = User('Tim', 'Tishkevich', 33, 'tut@tut.bo')
alex = User('Alex', 'Afanasyev', 30, 'afonya@pan.pl')
tim.greet_user()
tim.describe_user()
alex.greet_user()
alex.describe_user()
