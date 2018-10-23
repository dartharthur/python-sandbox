"""
Rotate an array of n elements to the right by k steps.
For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Source: https://leetcode.com/problems/rotate-array/description/
"""


def rotate_array_in_place(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    swap(nums, 0, 1)


def rotate_array_extra_space(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int] New list containing rotated nums.
    """
    len_nums = len(nums)
    positions = {}
    rotated_nums = []
    for idx, num in enumerate(nums):
        if (idx + k) >= len_nums:
            positions[num] = idx + k - len_nums
        else:
            positions[num] = idx + k
    sorted_pairs = sorted(positions.items(), key=sort_by_index)
    for pair in sorted_pairs:
        rotated_nums.append(pair[0])
    return rotated_nums


def sort_by_index(entry):
    """
    :type entry: Tuple(int, int)
    :rtype: int
    """
    return entry[1]


def swap(nums, index1, index2):
    """
    :type nums: List[int]
    :type index1: int
    :type index2: int
    :rtype: void Do not return anything, swap two positions in nums.
    """
    current = nums[index1]
    nums[index1] = nums[index2]
    nums[index2] = current
    print(nums)
