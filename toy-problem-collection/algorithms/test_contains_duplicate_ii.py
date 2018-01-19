import unittest
from contains_dupliate_ii import contains_nearby_duplicate


class TestContainsDuplicateII(unittest.TestCase):
    def test_contains_nearby_duplicate(self):
        self.assertEqual(contains_nearby_duplicate([], 0), False)
        self.assertEqual(contains_nearby_duplicate([99, 99], 2), True)
        self.assertEqual(contains_nearby_duplicate(
            [99, 1, 3, 4, 99], 2), False)
        self.assertEqual(contains_nearby_duplicate([1, 0, 1, 1], 1), True)
        self.assertEqual(contains_nearby_duplicate(
            [0, 1, 2, 3, 4, 0, 0, 7, 8, 9, 10, 11, 12, 0], 1), True)


if __name__ == '__main__':
    unittest.main()
