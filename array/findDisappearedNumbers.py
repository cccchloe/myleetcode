'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        counter = {}
        for i in range(len(nums)):
            counter[i+1] = 0
        for j in nums:
            counter[j] += 1
        nonappr = []
        for k, v in counter.items():
            if v == 0:
                nonappr.append(k)
        return nonappr