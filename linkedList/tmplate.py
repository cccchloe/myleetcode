class solution:
    def solve(self, head: ListNode):
        # Initialize slow & fast pointers
        slow = head
        fast = head
        '''
         * Change this condition to fit specific problem.
         * Attention: remember to avoid null-pointer error
        '''

        while slow != None and fast != None and fast.next != None :
            slow = slow.next           # move slow pointer one step each time
            fast = fast.next.next      # move fast pointer two steps each time
            if slow == fast :        # change this condition to fit specific problem
                return True

        return False   #change return value to fit specific problem
