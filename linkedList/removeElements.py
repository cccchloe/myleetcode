# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        while head is not None and head.val == val:
            head = head.next
        if head is None:
            return head
        prevNode = head
        curNode = head.next
        while curNode is not None:
            if curNode.val == val:
                prevNode.next = curNode.next
            else:
                prevNode = prevNode.next
            curNode = prevNode.next
        return head