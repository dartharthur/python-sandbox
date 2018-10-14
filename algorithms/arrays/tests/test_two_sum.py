import unittest
from two_sum import two_sum


class TestValidParentheses(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])


if __name__ == '__main__':
    unittest.main()
