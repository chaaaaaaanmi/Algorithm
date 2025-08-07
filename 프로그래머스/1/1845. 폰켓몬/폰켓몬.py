def solution(nums):
    nums_set = set(nums)
    result = min(len(nums_set), len(nums) // 2)
    return result