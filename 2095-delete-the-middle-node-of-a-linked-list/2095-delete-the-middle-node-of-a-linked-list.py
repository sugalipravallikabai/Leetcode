# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        pre = None
        slow = fast = head
        while fast and fast.next:
            pre = slow
            fast = fast.next.next
            slow = slow.next
        pre.next = slow.next
        return head