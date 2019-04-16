import my_class as mc
import unittest as ut
from my_class import MyClass

a = MyClass()
b = MyClass()

unittest.TestCase().assertEquals(a, b)
a == b
d = {}
d[a] = 5