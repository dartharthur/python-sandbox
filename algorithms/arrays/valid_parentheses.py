"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order,
"()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""


def valid_parentheses(string):
    """
    :type s: str
    :rtype: bool
    """
    legend = {
        ')': '(',
        '}': '{',
        ']': '[',
    }

    storage = []

    for char in string:
        if storage and legend.get(char) == storage[-1]:
            storage.pop()
        else:
            storage.append(char)

    if storage:
        return False
    else:
        return True
