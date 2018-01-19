"""
Given an array of integers and an integer k,
find out whether there are two distinct indices i and j in the array
such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Source: https://leetcode.com/problems/contains-duplicate-ii/description/
"""


def contains_nearby_duplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    lib = {}

    for idx, num in enumerate(nums):
        if lib.get(num):
            lib[num].append(idx)
        else:
            lib[num] = [idx]

    for indexes in lib.values():
        if len(indexes) > 1:
            for idx, num in enumerate(indexes):
                if idx + 1 < len(indexes) and indexes[idx + 1] - num <= k:
                    return True

    return False
