import unittest
from valid_parentheses import valid_parentheses

class TestValidParentheses(unittest.TestCase):
  def test_valid_parentheses(self):
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

if __name__ == '__main__':
  unittest.main()