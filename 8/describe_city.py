def describe_city(city: str,
                  country: str = 'iceland',
                  ):
    print(f'{city.title()} is {country.title()} ! ')


describe_city(city='manchester')
describe_city('reykjavik')
describe_city('minsk', 'belarus')
