# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return False
        if head.next is None:
            return True
        # step 1 get mid point and end point of list
        fast, slow = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        # step 2 reverse second half list
        newList = self.reverseList(slow)

        # step 3 compare each node
        ptA = head
        ptB = newList

        while ptB is not None:
            if ptA.val != ptB.val:
                return False
            ptA = ptA.next
            ptB = ptB.next

        if ptB is None:
            return True

    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur is not None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev