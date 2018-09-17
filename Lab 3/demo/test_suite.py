import unittest as ut

import test_primer1
import test_primer2

def suite():
    suite = ut.TestSuite()
    suite.addTests(ut.defaultTestLoader.loadTestsFromModule(test_primer1))
    suite.addTests(ut.defaultTestLoader.loadTestsFromModule(test_primer2))

    return suite

if __name__=='__main__':
    runner = ut.TextTestRunner(verbosity=2)
    runner.run(suite())