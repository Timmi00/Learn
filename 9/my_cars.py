from car import Car
from electric_car import ElectricCar as EC


my_beetle = Car('VW', 'beetle', 1980)
print(my_beetle.get_descriptive_name())
my_tesla = EC('tesla', 'cyber track', 2023)
print(my_tesla.get_descriptive_name())
