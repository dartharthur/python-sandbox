"""Functions needed to solve longest_unique_substring."""

def longest_unique_substring(s):
  """Given a string, find the length of the longest substring without repeating characters."""

  """
  :type s: str
  :rtype: int
  """
  longest = ''
  for i in range(len(s)):
    longestSoFar = check_substrings(s[i:])
    if len(longestSoFar) > len(longest):
      longest = longestSoFar
  print('Longest substring is', longest)
  return len(longest)

def check_substrings(s):
  """Given a substring of s, find the length of the longest substring without repeating characters."""

  """
  :type s: str
  :rtype: int
  """
  longest = ''
  for i in range(len(s)):
    if s[i] not in s[:i]:
      substring = s[:i + 1]
      if len(substring) > len(longest):
        longest = substring
    else:
      return longest
  return longest
