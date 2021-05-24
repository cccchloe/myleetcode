'''
Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.
'''
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maximums = set()
        for i in nums:
            maximums.add(i)
            if len(maximums) > 3:
                maximums.remove(min(maximums))
        if len(maximums) < 3:
            return max(maximums)
        else:
            return min(maximums)