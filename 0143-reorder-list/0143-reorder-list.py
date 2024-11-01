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
            return head
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
        first,second = head,pre
        while second.next:
            t = first.next
            first.next = second
            first = t
            t1 = second.next
            second.next = first
            second = t1
        