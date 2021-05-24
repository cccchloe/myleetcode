# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        prehead = ListNode(-1)
        prev = prehead
        tens = 0
        while l1 is not None or l2 is not None:
            print(prehead)
            if l1 is None and l2 is not None:
                ones = mod( l2.val + tens, 10)
                tens =  int((l2.val + tens)/10)
                l2 = l2.next
            elif l2 is None and l1 is not None:
                ones = mod( l1.val + tens, 10)
                tens =  int((l1.val + tens)/10)
                l1 = l1.next
            else:
                ones = mod(l1.val + l2.val + tens, 10)
                tens =  int((l1.val+l2.val + tens)/10)
                l1 = l1.next
                l2 = l2.next
            prev.next = ListNode(ones)
            prev = prev.next
        if tens > 0:
            prev.next = ListNode(tens)
        return prehead.next