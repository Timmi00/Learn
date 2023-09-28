import unittest
from worker import Emploee
from random import randint


class TestEmploee(unittest.TestCase):
    """Test for Emploee class"""

    def setUp(self) -> None:
        """Make class instance"""
        self.my_worker = Emploee('Alex', 'Spam', 500)

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
