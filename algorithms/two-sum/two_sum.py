def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    addendMap = {}
    for i, num in enumerate(nums):
        diff = target - num
        if num in addendMap and addendMap[num] != i:
            return [addendMap[num], i]
        addendMap[diff] = i
    return []