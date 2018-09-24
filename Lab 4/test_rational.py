import unittest as ut

from rational import Rational

class TestRational(ut.TestCase):

    def test_simplify(self):
        r = Rational(7, 35)
        self.assertEqual(r, Rational(2, 10))
        self.assertEqual(r.n, 1)
        self.assertEqual(r.d, 5)

ut.main()