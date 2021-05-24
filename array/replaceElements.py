class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        '''
        Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

        After doing so, return the array.
        '''
        if len(arr) ==1:
            arr[0] = -1
        n = len(arr) -1
        max_num = arr[n]

        while n >= 0:
            if n == (len(arr) - 1):
                arr[n] = -1
                n -= 1
            else:
                temp = arr[n]
                arr[n] = max_num
                max_num = max(max_num, temp)
                n -= 1
        return arr