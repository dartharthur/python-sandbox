import unittest
from pascal_triangle import generate_triangle, generate_row


class TestPascalTriangle(unittest.TestCase):
    def test_generate_row(self):
        self.assertEqual(generate_row([1, 1], 3), [1, 2, 1])
        self.assertEqual(generate_row([1, 2, 1], 4), [1, 3, 3, 1])
        self.assertEqual(generate_row([1, 3, 3, 1], 5), [1, 4, 6, 4, 1])

    def test_pascal_triangle(self):
        self.assertEqual(generate_triangle(0), [])
        self.assertEqual(generate_triangle(1), [[1]])
        self.assertEqual(generate_triangle(2), [[1], [1, 1]])
        self.assertEqual(generate_triangle(3), [[1], [1, 1], [1, 2, 1]])
        self.assertEqual(generate_triangle(
            4), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])
        self.assertEqual(generate_triangle(
            5), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])


if __name__ == '__main__':
    unittest.main()
