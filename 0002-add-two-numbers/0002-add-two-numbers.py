# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t1 = l1
        t2 = l2
        dummy = ListNode(-1)
        t = dummy
        carry = 0
        while t1 or t2:
            tol = carry
            if t1:
                tol += t1.val
                t1 = t1.next
            if t2:
                tol += t2.val
                t2 = t2.next
            data = tol%10
            t.next=ListNode(data)
            t = t.next
            carry = tol//10
        if carry != 0:
            t.next = ListNode(carry) 
        return dummy.next
        