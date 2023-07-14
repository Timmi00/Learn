class Car:
    """БАЗОВАЯ МОДЕЛЬ АВТОМОБИЛЯ"""

    def __init__(self, make: str, model: str, year: int):
        """Иннициализация атрибутов описания"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает отформатированное описание"""
        long_name: str = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        """Вывод пробега в кМ"""
        print(f'This car has {self.odometer_reading} kM on it.')

    def update_odometer(self, mileage: int):
        """Устанавливаем заданное значение на одометре"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can\'t roll back odometer!')

    def increment_odometer(self, miles: int):
        """Увеличваем показания одометра на заданное значение"""
        self.odometer_reading += miles


class Battery:
    def __init__(self, size: int = 75):
        self.size = size

    def describe_battery(self):
        print(f'This car has a {self.size}-kWh battery')


class ElectricCar(Car):

    def __init__(self, make: str, model: str, year: int):
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
