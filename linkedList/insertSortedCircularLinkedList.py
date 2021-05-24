"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if head is None:
            newNode = Node(insertVal)
            newNode.next = newNode
            return newNode
        prev = head
        cur = head.next
        insertflag = False
        while True:
            if prev.val <= insertVal <= cur.val:
                insertflag = True

            elif prev.val > cur.val:
                if insertVal >= prev.val or insertVal <= cur.val:
                    insertflag = True

            if insertflag:
                prev.next = Node(insertVal, cur)
                return head

            prev = prev.next
            cur = cur.next

            if prev == head:
                break
        prev.next = Node(insertVal, cur)
        return head