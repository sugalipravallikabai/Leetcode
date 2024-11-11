# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        s = f = head
        while f and f.next:
            s = s.next
            f = f.next.next
        cur,pre = s,None
        while cur:
            t = cur.next
            cur.next = pre
            pre = cur
            cur = t
        f,s = head,pre
        while s.next:
            temp = f.next
            t = s.next
            f.next = s
            s.next = temp
            f = temp
            s = t
        