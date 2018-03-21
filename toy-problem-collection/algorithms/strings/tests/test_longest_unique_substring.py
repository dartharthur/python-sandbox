import unittest
from longest_unique_substring import longest_unique_substring


class TestContainsDuplicate(unittest.TestCase):
    def test_longest_unique_substring(self):
        self.assertEqual(longest_unique_substring("abcabcbb"), 3)
        self.assertEqual(longest_unique_substring("bbbbb"), 1)
        self.assertEqual(longest_unique_substring("pwwkew"), 3)


if __name__ == '__main__':
    unittest.main()
