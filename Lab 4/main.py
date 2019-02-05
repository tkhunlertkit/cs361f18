import unittest

from matthewRationalMethods import MatthewRationalMethods
from tylerRationalMethods import TylerRationalMethods
from maxRationalMethods import MaxRationalMethods
from jasRationalMethods import JasRationalMethods
from samRationalMethods import SamRationalMethods

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(MatthewRationalMethods))
suite.addTest(unittest.makeSuite(TylerRationalMethods))
suite.addTest(unittest.makeSuite(MaxRationalMethods))
suite.addTest(unittest.makeSuite(JasRationalMethods))
suite.addTest(unittest.makeSuite(SamRationalMethods))

res = unittest.TextTestRunner().run(suite)
print(res)
print("*"*20)
for i in res.failures: print(i[1])
