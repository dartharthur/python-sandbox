"""Functions needed to solve longest_unique_substring."""

def longest_unique_substring(s):
  """Given a string, find the length of the longest substring without repeating characters."""

  """
  :type s: str
  :rtype: int
  """
  allSubstrings = []
  longest = 0
  for i in range(len(s)):
    batch = findSubstrings(s[i:])
    allSubstrings += batch[0]
    if len(batch[1]) > longest:
      longest = len(batch[1])
  print('here', longest)
  return longest

def findSubstrings(s):
  """Given a string, find all of the substrings without repeating characters."""

  """
  :type s: str
  :rtype: List[str]
  """
  substrings = []
  longest = ''
  for i in range(len(s)):
    if s[i] not in s[:i]:
      substring = s[:i + 1]
      substrings.append(substring)
      if len(substring) > len(longest):
        longest = substring
    else:
      return (substrings, longest)
  return (substrings, longest)