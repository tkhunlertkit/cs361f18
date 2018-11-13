import unittest
from rational import Rational

class MaxRationalMethods(unittest.TestCase):

   # From Max Lowery
   def test_sub1(self): # Tests that 3/5 - 1/5 = 2/5
     rat1 = Rational(3, 5)
     rat2 = Rational(1, 5)
     self.assertEqual((rat1-rat2).n, 2)
     self.assertEqual((rat1-rat2).d, 5)

   # From Max Lowery
   def test_sub2(self): # Tests that 3/2 - 4/2 = -1/2
     rat1 = Rational(3, 2)
     rat2 = Rational(4, 2)
     self.assertEqual((rat1-rat2).n, -1)
     self.assertEqual((rat1-rat2).d, 2)

    # From Max Lowery
   def test_add1(self): # Tests associative property of addition using -1/6 + 4/6 = 4/6 + -1/6
     rat1 = Rational(-1, 6)
     rat2 = Rational(4, 6)
     self.assertEqual((rat1+rat2).n, (rat2+rat1).n)
     self.assertEqual((rat1+rat2).d, (rat2+rat1).d)
