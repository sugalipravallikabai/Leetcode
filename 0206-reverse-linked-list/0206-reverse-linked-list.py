# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        temp = head
        pre = temp
        after = head.next
        while temp.next and after:
            temp = after
            after = after.next
            temp.next = pre
            pre = temp
        head.next = None
        head = pre
        return head