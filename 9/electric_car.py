from car import Car


class Battery:
    def __init__(self, size: int = 75):
        self.size = size

    def describe_battery(self):
        print(f'This car has a {self.size}-kWh battery')

    def get_range(self):
        rang = 0
        if self.size == 75:
            rang = 260
        elif self.size == 100:
            rang = 315
        print(f'This car can go about {rang} kM on a full charge')

    def upgrade_battery(self):
        if self.size != 100:
            self.size = 100


class ElectricCar(Car):

    def __init__(self, make: str, model: str, year: int):
        super().__init__(make, model, year)
        self.battery = Battery()
