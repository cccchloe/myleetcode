# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.
'''
class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        if head == None or head.next == None or head.next.next == None  :
            return False
        fast = head.next.next
        slow = head.next

        while fast != slow and fast.next != None and fast.next.next != None :
            fast = fast.next.next
            slow = slow.next
        if fast == slow:
            return True
        else:
            return False