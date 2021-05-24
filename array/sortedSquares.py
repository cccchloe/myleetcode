# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        idx = len(nums) -1
        # 建立定长的array
        s = [0] * len(nums)
        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                s[idx] = nums[r]**2
                r -= 1
                idx -=1
            elif abs(nums[l]) >= abs(nums[r]):
                s[idx] = nums[l]**2
                l += 1
                idx -=1
        return s