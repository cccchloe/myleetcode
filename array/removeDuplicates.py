class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        j = 0
        for i in range(1, len(nums)):
            if nums[j] == nums[i]:
                i += 1
            else:
                nums[j + 1] = nums[i]
                j += 1

        return j + 1