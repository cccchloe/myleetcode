class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        '''
        暴力解法： linear search
        '''
        if (arr == None) or (len(arr) == 0):
            return False
        expect = {}
        for i in range(0,len(arr)):

            for j in range(i+1, len(arr)):
                if (arr[j] == arr[i]*2):
                    return True
                elif (arr[i] %2 == 0) and (arr[j] == arr[i]/2):
                    return True
        return False