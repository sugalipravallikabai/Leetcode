# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        n1,n2 = 0,0
        t1 = headA
        t2 = headB
        while t1 or t2:
            if t1:
                n1+=1
                t1 = t1.next
            if t2:
                n2+=1
                t2=t2.next
        temp1,temp2 = headA,headB
        if n1 > n2:
            for i in range(n1-n2):
                temp1 = temp1.next
        else:
            for i in range(n2-n1):
                temp2 = temp2.next
        while temp1 and temp2:
            if temp1 == temp2:
                return temp1
            temp1 = temp1.next
            temp2 = temp2.next
        return None
                