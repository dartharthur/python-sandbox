def valid_parentheses(s):
  legend = {
    ')': '(',
    '}': '{',
    ']': '[',
  }
  
  storage = []

  for char in s:
    if storage and legend.get(char) == storage[-1]:
      storage.pop()
    else:
      storage.append(char)
  
  if storage:
    return False
  else:
    return True