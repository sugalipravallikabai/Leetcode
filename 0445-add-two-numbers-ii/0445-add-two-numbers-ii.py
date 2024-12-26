# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            pre = None
            temp = head
            while temp:
                after = temp.next
                temp.next = pre
                pre = temp
                temp = after
            head = pre
            return head
        l1 = reverse(l1)
        l2 = reverse(l2)
        carry = 0
        dummy = ListNode(-1)
        temp = dummy
        h1,h2 = l1,l2
        while h1 and h2:
            tol = carry+h1.val+h2.val
            carry = tol//10
            data = tol%10
            temp.next = ListNode(data)
            temp = temp.next
            h1 = h1.next
            h2 = h2.next
        while h1:
            tol = carry+h1.val
            carry = tol//10
            data = tol%10
            temp.next = ListNode(data)
            temp = temp.next
            h1 = h1.next
        while h2:
            tol = carry+h2.val
            carry = tol//10
            data = tol%10
            temp.next = ListNode(data)
            temp = temp.next
            h2 = h2.next
        if carry != 0:
            temp.next = ListNode(carry)
            temp = temp.next
        head = reverse(dummy.next)


        return head