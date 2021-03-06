# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # Create a new ListNode as head of returned linked list
        new_list_start = ListNode(0)
        curr = new_list_start
        carry = 0
        
        while l1 or l2 or carry:
            
            # Check whether the current node is None, if true, assign it to the variable, otherwise the variable value is 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # The divmod() method takes two numbers and returns a pair of numbers (a tuple) consisting of their quotient and remainder.
            carry, out = divmod(v1 + v2 + carry, 10)
            
            curr.next = ListNode(out)
            curr = curr.next
            
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        
        
        return new_list_start.next