import unittest
from app import calc_arif_p

class TestArifProgression(unittest.TestCase):
    
    def test_basic_progression(self):
        expected = [2, 4, 6, 8, 10]
        self.assertEqual(calc_arif_p(2, 5), expected)

    def test_single_element(self):
        expected = [5]
        self.assertEqual(calc_arif_p(5, 1), expected)

    def test_zero_iterations(self):
        self.assertEqual(calc_arif_p(10, 0), [])

    def test_negative_numbers(self):
        expected = [-3, -6, -9]
        self.assertEqual(calc_arif_p(-3, 3), expected)

if __name__ == '__main__':
    unittest.main()