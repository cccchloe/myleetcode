class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # modify in place, return length of new array
        # move all ele not equals to specified value to left
        # two pointers: one point move along the list , one point to the new list idx
        l = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                i += 1
            else:
                nums[l] = nums[i]
                i += 1
                l += 1
        return l