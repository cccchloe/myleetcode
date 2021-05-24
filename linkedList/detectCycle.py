# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null
'''
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return None
        fast, slow = head, head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if fast == None or fast.next == None:
            return None
        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return fast