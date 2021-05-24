from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        temp=arr.copy()
        orig_idx=0
        tmp_idx=0
        while orig_idx<len(arr):
            arr[orig_idx]=temp[tmp_idx]
            if temp[tmp_idx]!=0:
                orig_idx+=1
                tmp_idx+=1
            else:
                if orig_idx < len(arr) -1:
                    arr[orig_idx+1]=0
                orig_idx+=2
                tmp_idx+=1
