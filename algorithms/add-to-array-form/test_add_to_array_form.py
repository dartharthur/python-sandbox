import unittest

from add_to_array_form import add_to_array_form


class TestContainsDuplicate(unittest.TestCase):
    def test_add_to_array_form(self):
        self.assertEqual(add_to_array_form([1,2,0,0], 34), [1,2,3,4])
    def test_add_to_array_form(self):
        self.assertEqual(
            add_to_array_form(
                [2,0,8,1,1,5,1,6,3,3,0,1,1,1,5,0,9,8,6,1,4,9,9,9,7,9,8,8,7,7,8,4,7,3,3,6,4,0,2,9,6,9,8,9,1,2,0,7,1,3,3,8,6,3,7,1,5,6,0,2,0,9,5,9,3,3,0,0,4,7,9,7,3,0,1,0,5,6,3,5,3,4,0,7,9,4,6,9,7,7,1,1,8,3,9,4,5,9,0,9,9,4,2,4,7,8,2,5,7,5,5,0,0,4,6,4,2,2,9,5,3,0,5,0,7,5,1,2,2,6,3,8,6,0,4,7,1,1,7,6,6,1,1,7,4,7,5,9,6,8,7,8,8,7,5,6,7,7,4,8,4,5,0,4,6,0,0,8,9,6,7,7,2,6,4,2,9,1,3,5,1,0,4,8,5,0,6,8,5,2,1,8,7,6,6,8,9,7,2,2,7,9,8,7,1,2,2,6,7,4,9,4,6,9,9,4,5,8,7,0,8,4,3,6,2,0,4,6,3,5,7,2,0,6,3,9,1,2,9,3,0,0,8,8,5,9,8,4,5,6,5,2,5,7,3,0,2,0,4,0,6,3,5,6,5,3,1,3,4,4,0,9,4,3,3,2,2,5,8,8,0,6,0,1,1,2,4,6,2,8,7,2,2,9,0,3,2,1,5,0,4,3,8,5,1,2,8,5,6,4,5,9,1,1,8,9,9,8,4,7,4,8,5,3,9,1,3,2,7,2,7,1,9,0,4,5,2,9,4,1,9,8,2,0,8,1,5,4,9,7,4,0,3,1,4,9,9,5,2,3,1,3,7,7,4,7,7,6,2,0,1,9,4,9,7,9,9,0,4,6,4,0,2,7,5,3,2,1,0,5,4,0,7,9,5,2,5,5,1,3,6,7,4,6,6,2,7,5,8,6,7,5,4,9,4,3,6,6,7,4,6,7,6,5,6,0,2,7,3,6,9,9,0,8,0,4,2,7,6,8,5,1,0,7,0,5,4,4,1,8,1,5,7,9,0,8,4,2,7,9,7,8,4,6,0,0,1,6,9,7,1,6,5,4,4,8,3,2,7,1,5,5,4,2,8,7,6,1,9,5,8,1,4,7,0,4,9,0,8,8], 
                730
            ),
            [2,0,8,1,1,5,1,6,3,3,0,1,1,1,5,0,9,8,6,1,4,9,9,9,7,9,8,8,7,7,8,4,7,3,3,6,4,0,2,9,6,9,8,9,1,2,0,7,1,3,3,8,6,3,7,1,5,6,0,2,0,9,5,9,3,3,0,0,4,7,9,7,3,0,1,0,5,6,3,5,3,4,0,7,9,4,6,9,7,7,1,1,8,3,9,4,5,9,0,9,9,4,2,4,7,8,2,5,7,5,5,0,0,4,6,4,2,2,9,5,3,0,5,0,7,5,1,2,2,6,3,8,6,0,4,7,1,1,7,6,6,1,1,7,4,7,5,9,6,8,7,8,8,7,5,6,7,7,4,8,4,5,0,4,6,0,0,8,9,6,7,7,2,6,4,2,9,1,3,5,1,0,4,8,5,0,6,8,5,2,1,8,7,6,6,8,9,7,2,2,7,9,8,7,1,2,2,6,7,4,9,4,6,9,9,4,5,8,7,0,8,4,3,6,2,0,4,6,3,5,7,2,0,6,3,9,1,2,9,3,0,0,8,8,5,9,8,4,5,6,5,2,5,7,3,0,2,0,4,0,6,3,5,6,5,3,1,3,4,4,0,9,4,3,3,2,2,5,8,8,0,6,0,1,1,2,4,6,2,8,7,2,2,9,0,3,2,1,5,0,4,3,8,5,1,2,8,5,6,4,5,9,1,1,8,9,9,8,4,7,4,8,5,3,9,1,3,2,7,2,7,1,9,0,4,5,2,9,4,1,9,8,2,0,8,1,5,4,9,7,4,0,3,1,4,9,9,5,2,3,1,3,7,7,4,7,7,6,2,0,1,9,4,9,7,9,9,0,4,6,4,0,2,7,5,3,2,1,0,5,4,0,7,9,5,2,5,5,1,3,6,7,4,6,6,2,7,5,8,6,7,5,4,9,4,3,6,6,7,4,6,7,6,5,6,0,2,7,3,6,9,9,0,8,0,4,2,7,6,8,5,1,0,7,0,5,4,4,1,8,1,5,7,9,0,8,4,2,7,9,7,8,4,6,0,0,1,6,9,7,1,6,5,4,4,8,3,2,7,1,5,5,4,2,8,7,6,1,9,5,8,1,4,7,0,4,9,8,1,8]
        )

if __name__ == '__main__':
    unittest.main()