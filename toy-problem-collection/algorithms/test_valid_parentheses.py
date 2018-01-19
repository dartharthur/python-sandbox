import unittest
from valid_parentheses import valid_parentheses


class TestValidParentheses(unittest.TestCase):
    def test_valid_parentheses(self):
<<<<<<< HEAD
        result1 = valid_parentheses('()')
        self.assertEqual(result1, True)
        result2 = valid_parentheses(')(')
        self.assertEqual(result2, False)
        result3 = valid_parentheses('{()}')
        self.assertEqual(result2, False)
        result4 = valid_parentheses('(]')
        self.assertEqual(result4, False)
        result5 = valid_parentheses('([)]')
        self.assertEqual(result5, False)

=======
        self.assertEqual(valid_parentheses('()'), True)
        self.assertEqual(valid_parentheses(')('), False)
        self.assertEqual(valid_parentheses('{()}'), False)
        self.assertEqual(valid_parentheses('(]'), False)
        self.assertEqual(valid_parentheses('([)]'), False)
>>>>>>> 28035623e3a4a5f413a338f1a16f56290dd534d5

if __name__ == '__main__':
    unittest.main()
