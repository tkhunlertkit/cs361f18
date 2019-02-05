import unittest as ut

from primer import Primer

class TestPrimer2(ut.TestCase):

    def setUp(self):
        self.primer = Primer(7)

    def test_generate_0(self):
        expected = list(self.primer.generate(0))
        self.assertEqual(expected, [])

    def test_generate_num_within_limit(self):
        expected = list(self.primer.generate(2))
        self.assertEqual(expected, [2, 3])

    @ut.skip('not now')
    def test_generate_num_exact_limit(self):
        expected = list(self.primer.generate(4))
        self.assertEqual(expected, [2, 3, 5, 7])

    def test_generate_num_exceed_limit(self):
        expected = list(self.primer.generate(5))
        self.assertEqual(expected, [2, 3, 5, 7])
