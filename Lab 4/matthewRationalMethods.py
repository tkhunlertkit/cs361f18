import unittest
from rational import Rational

class MatthewRationalMethods(unittest.TestCase):

    # matthew 
   def test_string_one( self ):
      result = Rational().__str__()
      self.assertEqual('0/1', result)

   # matthew
   def test_string_two( self ):
      result = Rational().__str__()
      self.assertEqual('0', result[0])
      self.assertEqual('/', result[1])
      self.assertEqual('1', result[2])

   # matthew
   def test_float_one( self ):
      result = Rational().__float__()
      self.assertEqual(0.0, result)
