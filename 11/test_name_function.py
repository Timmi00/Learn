import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Тесты для name_function.py"""

    def test_first_last_name(self):
        """Имена вида 'Иван Иванькоф' работают правильно?"""
        formatted_name: str = get_formatted_name(
            'иван', 'Иванькоф'
        )
        self.assertEqual(formatted_name, 'Иван Иванькоф')

    def test_first_last_middle_name(self):
        """Имена вида 'Иван Иваныч Иванькоф' работают правильно?"""
        formatted_name: str = get_formatted_name(
            'иван', 'Иванькоф', 'Иваныч'
        )
        self.assertEqual(
            formatted_name, 'Иван Иваныч Иванькоф'
        )


if __name__ == '__main__':
    unittest.main()
