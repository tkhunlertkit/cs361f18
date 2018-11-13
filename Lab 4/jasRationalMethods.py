import unittest
from rational import Rational

class JasRationalMethods(unittest.TestCase):

     # Jas
   def test_init1(self):
      r = Rational(1,2)
      self.assertIs(r.n, 1)
      self.assertIs(r.d, 2)

   # Jas
   def test_init2(self):
      r = Rational(1,-2)
      self.assertTrue(r.d!=-2)

   # Jas
   def test_add(self):
      a = Rational(1,2)
      b = Rational(1,2)
      c = a+b
      self.assertFalse(c.n,2)
      self.assertFalse(c.d,4)
      self.assertTrue(c.n,1)
      self.assertTrue(c.d,1)