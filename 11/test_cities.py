import unittest
from city_functions import get_formatted_name


class CapitalsTestCase(unittest.TestCase):
    """Тесты для city_functions.py"""
    def test_country_capital(self):
        formatted_name: str = get_formatted_name(
            'менск',
            'Беларусь',
        )
        self.assertEqual(formatted_name, 'Беларусь Менск')

    def test_country_capital_population(self):
        formatted_name: str = get_formatted_name(
            'менск',
            'Беларусь',
            10000000
        )
        self.assertEqual(formatted_name, 'Беларусь Менск 10000000')


if __name__ == '__main__':
    unittest.main()
