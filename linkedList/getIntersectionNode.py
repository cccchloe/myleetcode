# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # Method 1 hash table
        #         Time : O(N+M)   Space: O(M) - M=size of headB
        #         nodes_b = set()

        #         while headB is not None:
        #             nodes_b.add(headB)
        #             headB = headB.next

        #         while headA is not None:
        #             if headA in nodes_b:
        #                 return headA
        #             else:
        #                 headA = headA.next

        #         return None

        # Method 2 Two pointers
        if headA is None or headB is None:
            return None

        pA = headA
        pB = headB

        while pA != pB:
            # if either pointer hits the end, switch head and continue the second traversal,
            # if not hit the end, just move on to next
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next

        return pA
    # the idea is if you switch head, the possible difference between length would be countered.
    # On the second traversal, they either hit or miss.
    # if they meet, pa or pb would be the node we are looking for,
    # if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them is the same,None
