import unittest
from rational import Rational

class TylerRationalMethods(unittest.TestCase):

   # tyler
   def test_divide1(self):
      """Divide test case one, throw exception if other.n is zero"""
      n = Rational(1, 1)
      d = Rational(0, 1)
      with self.assertRaises(ZeroDivisionError):
        """Divide by zero"""
        n.__div__(d)

   # tyler
   def test_divide2(self):
      """Identity Division Case"""
      n = Rational(2, 1)
      d = Rational(1, 1)
      result = n.__div__(d)
      self.assertEqual(n.n, result.n)
      self.assertEqual(n.d, result.d)

   # tyler
   def test_divide3(self):
      """Real Division Test Case"""
      n = Rational(5, 2)
      d = Rational(5, 2)
      result = n.__div__(d)
      self.assertEqual(result.n, 1)
      self.assertEqual(result.d, 1)

