import unittest
from rational import Rational

class SamRationalMethods(unittest.TestCase):

   # Sam
   def test_zero(self):
      # test if zero times zero
      zero = Rational(0,1)
      new = zero*zero
      self.assertEqual(new.n, 0)
      self.assertEqual(new.d, 1)
    
   # Sam
   def test_neg(self):
      #make sure multiply by negative comes out correctly
      neg = Rational(-1,1)
      mult = neg*(neg)
      self.assertEqual(mult.n, -1)
      self.assertEqual(mult.d, 1)
    
   # Sam
   def test_float(self):
      #test if rational floated is not instance of int or string
      res = Rational()
      self.assertFalse(isinstance(float(res), int))
      self.assertFalse(isinstance(float(res), str))
