class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[0:m].copy()
        idx_tmp = 0
        idx1 = 0
        idx2 = 0
        while idx1 < (m+n):
            if idx2 >= n:
                nums1[idx1] = temp[idx_tmp]
                idx_tmp += 1
                idx1 += 1
            elif idx_tmp >= m:
                nums1[idx1] = nums2[idx2]
                idx1 += 1
                idx2 += 1
            else:
                if temp[idx_tmp] <= nums2[idx2]:
                    nums1[idx1] = temp[idx_tmp]
                    idx1 += 1
                    idx_tmp += 1
                else:
                    nums1[idx1] = nums2[idx2]
                    idx1 += 1
                    idx2 += 1