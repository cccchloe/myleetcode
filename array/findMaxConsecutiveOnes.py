# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        maxcount = 0
        l = 0
        while l < len(nums):
            if nums[l] == 1:
                r = l + 1
                while r < len(nums):
                    if nums[r] == 0:
                        maxcount = max(maxcount, r-l)
                        break
                    else:
                        r += 1
                # 边界情况 [0,1], [0,0],[0],[1]
                # 此时r>len, 无法进入循环，所以直接得到maxcount
                maxcount = max(maxcount, r-l)
                l = r + 1
            else:
                l += 1
        return maxcount
