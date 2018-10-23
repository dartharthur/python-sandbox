import unittest

from contains_duplicate import contains_duplicate


class TestContainsDuplicate(unittest.TestCase):
    def test_contains_duplicate(self):
        self.assertEqual(contains_duplicate([]), False)
        self.assertEqual(contains_duplicate([99, 99]), True)
        self.assertEqual(contains_duplicate(
            [99, 1, 3, 4, 99]), True)
        self.assertEqual(contains_duplicate([1, 0, 1, 1]), True)
        self.assertEqual(contains_duplicate(
            [0, 1, 2, 3, 4, 0, 0, 7, 8, 9, 10, 11, 12, 0]), True)
        self.assertEqual(contains_duplicate([0, 1, 2, 3]), False)


if __name__ == '__main__':
    unittest.main()
