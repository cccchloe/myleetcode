class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = 0
        right = 0
        while right < n:
            if nums[right] == 0:
                right += 1
            else:
                nums[left] = nums[right]
                left += 1
                right += 1
        for i in range(left,n):
            nums[i] = 0