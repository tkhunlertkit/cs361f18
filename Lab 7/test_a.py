import unittest

from a import A
from b_mocked import BMocked

class TestA(unittest.TestCase):

    def test_init_a(self):
        # What do we do?
        test_b = BMocked()
        test_a1 = A(test_b)
        test_a2 = A(test_b)
        test_a.b.method_b1()
        test_a.method_a1()
        test_a1 == test_a2
        test_a1.__eq__(test_a2)
        self.assertEq
        pass


