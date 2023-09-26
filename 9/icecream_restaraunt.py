from restaurant import Restaurant


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name: str, cuisine_type: str, flavors: list):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def describe_flavors(self):
        print('The restaurant have next flavors:')
        for flavor in self.flavors:
            print(flavor)


mor = IceCreamStand('kafe_morozhenoe', 'all kinds of icecream', ['peach', 'mellon', 'chocolate'])
mor.describe_flavors()
mor.describe_restaurant()
mor.open_restaurant()
