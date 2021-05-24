'''
    Input: [1,0,1,1,0]
    Output: 4
    Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
    '''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longestSquence = 0
        numZeros = 0
        left, right = 0,0
        while right < len(nums): # while our window is in bounds
            if nums[right] == 0 :  # add the right most element into our window
                numZeros += 1
            while numZeros == 2: # if our window is invalid, contract our window
                if nums[left] == 0:
                    numZeros -= 1
                left += 1
            longestSquence =  max(longestSquence, right - left + 1) # update our longest sequence answer
            right += 1
        return max(longestSquence,1)