import unittest
from worker import Employee
from random import randint


class TestEmployee(unittest.TestCase):
    """Test for Employee class"""

    def setUp(self) -> None:
        """Make class instance"""
        self.my_worker = Employee('Alex', 'Spam', 500)

    def test_give_default_raise(self):
        """Check correct raising"""
        self.my_worker.give_raise()
        self.assertEqual(self.my_worker.fee, 1000)

    def test_give_custom_raise(self):
        """Check correct custom raising"""
        fee: int = randint(0, 9999999)
        self.my_worker.give_raise(fee)
        self.assertEqual(self.my_worker.fee, (500 + fee))

    if __name__ == '__main__':
        unittest.main()
