# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        Approach 1: two pointers (Iterative)
        '''
        prev = None
        cur = head
        while cur is not None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

        '''
        Approach 2: recursive
        '''
        if head is None or head.next is None:
            return head
        rest = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return rest
