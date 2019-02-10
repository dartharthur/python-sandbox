### Solution 1 ###

import math

def add_to_array_form(A: 'List[int]', K: 'int') -> 'List[int]':
    a_to_num = array_form_to_num(A)
    num = a_to_num + K
    return integer_to_array_form(num)

def array_form_to_num( A: 'List[int]') -> 'int':
    if len(A) == 1:
        return A[0]
    
    factor = 1
    total = 0
    for num in reversed(A):
        total += (factor * num)
        factor *= 10
    
    return total

def integer_to_array_form( i: 'int') -> 'List[int]':
    num = i
    a = []

    if (num == 0):
        return [0]

    while(num):
        b = num % 10
        a.append(b)
        # num = math.floor(num / 10)
        # OverflowError: integer division result too large for a float
        # https://stackoverflow.com/questions/27946595/how-to-manage-division-of-huge-numbers-in-python
        # In python3, num / 10 tries to return a float but floats can't be arbitrarily large.
        # Use // to get an integer back from the division.
        num = num // 10

    return list(reversed(a))

### Solution 2 ###

"""
https://leetcode.com/problems/add-to-array-form-of-integer/discuss/234497/Short-and-Simple-Python
"""
def add_to_array_form(A: 'List[int]', K: 'int') -> 'List[int]':
    A = int(''.join([str(x) for x in A]))
    return [int(x) for x in list(str(A + K))]
