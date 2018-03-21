import unittest
from max_profit import max_profit


class TestContainsDuplicate(unittest.TestCase):
    def test_max_profit(self):
        self.assertEqual(max_profit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(max_profit([7, 6, 4, 3, 1]), 0)
        self.assertEqual(max_profit([2, 4, 1, 6]), 5)
        self.assertEqual(max_profit([2, 4, 1]), 2)
        self.assertEqual(max_profit([2, 4, 6, 1]), 4)
        self.assertEqual(max_profit([3, 2, 6, 5, 0, 3]), 4)


if __name__ == '__main__':
    unittest.main()
