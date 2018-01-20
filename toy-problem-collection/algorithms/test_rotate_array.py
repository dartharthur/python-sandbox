import unittest
from rotate_array import rotate_array_in_place, rotate_array_extra_space


class TestRotateArray(unittest.TestCase):
    # def test_rotate_array_in_place(self):
    #     alpha = [1, 2, 3]
    #     rotate_array_in_place(alpha, 1)
    #     self.assertEqual(alpha, [3, 1, 2])

    def test_rotate_array_extra_space(self):
        self.assertEqual(rotate_array_extra_space([1, 2, 3], 1), [3, 1, 2])
        self.assertEqual(rotate_array_extra_space(
            [1, 2, 3, 4], 1), [4, 1, 2, 3])
        self.assertEqual(rotate_array_extra_space(
            [1, 2, 3, 4, 5, 6, 7], 3), [5, 6, 7, 1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
