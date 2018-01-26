"""
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
"""


def contains_duplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    lib = set()

    for num in nums:
        if num in lib:
            return True
        else:
            lib.add(num)

    return False
