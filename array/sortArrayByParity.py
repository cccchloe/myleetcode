class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if len(A) <=1:
            return A
        target = A.copy()
        idx = 0
        idx_tgt = 0
        n = len(target) - 1
        while idx < len(A):
            if A[idx] % 2 == 0:
                target[idx_tgt] = A[idx]
                idx += 1
                idx_tgt += 1
            else:
                target[n] = A[idx]
                n -= 1
                idx += 1
        return target