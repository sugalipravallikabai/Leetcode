# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        pre,cur = dummy,head
        
        while cur and cur.next:
            after = cur.next.next
            second = cur.next
            second.next = cur
            cur.next = after
            pre.next = second
            
            pre = cur
            cur = after
        return dummy.next