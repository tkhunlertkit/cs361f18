import unittest as ut

from primer import Primer

class TestPrimer1(ut.TestCase):

    def setUp(self):
        self.primer = Primer(7)

    def test_check_prime(self):
        self.assertTrue(self.primer.check_prime(2))
        self.assertTrue(self.primer.check_prime(3))
        self.assertTrue(self.primer.check_prime(5))
        self.assertFalse(self.primer.check_prime(10))
