# Given an array nums of integers, return how many of them contain an even number of digits.
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def dividTen(num: int):
            if num < 10:
                return 1
            return dividTen(num / 10) + 1

        even = 0
        for i in nums:
            if dividTen(i) % 2 == 0:
                even += 1
        return even
