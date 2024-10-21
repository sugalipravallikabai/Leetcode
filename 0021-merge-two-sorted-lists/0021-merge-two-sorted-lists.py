# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        t1 = dummy
        n1=0
        n2=0
        h1 = l1
        h2 = l2
        while h1 :
            n1+=1
            h1 = h1.next
        while h2:
            n2 += 1
            h2 = h2.next
        h1,h2 = l1,l2
        while n1 > 0 and n2 > 0:
            if h1.val <= h2.val:
                t1.next = h1
                t1 = h1
                h1 = h1.next
                n1 -= 1
            else:
                t1.next = h2
                t1=h2
                h2 = h2.next
                n2 -= 1
        while n1 > 0:
            t1.next = h1
            t1 = h1
            h1 = h1.next
            n1 -= 1
        while n2 > 0:
            t1.next = h2
            t1 = h2
            h2 = h2.next
            n2 -= 1
        
        return dummy.next
                
        