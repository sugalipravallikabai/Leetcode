# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t1 = l1
        t2 = l2
        s1 = []
        s2 = []
        ans =[]
        while t1:
            s1.append(t1.val)
            t1 = t1.next
        while t2:
            s2.append(t2.val)
            t2 = t2.next
        carry = 0
        while s1 or s2 or carry:
            x = s1.pop() if s1 else 0
            y = s2.pop() if s2 else 0
            summ = x+y+carry
            ans.append(summ%10)
            carry = summ//10
        head = ListNode(0)
        cur = head
        while ans:
            cur.next = ListNode(ans.pop())
            cur = cur.next
        return head.next