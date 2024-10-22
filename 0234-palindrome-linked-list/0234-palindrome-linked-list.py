# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ans = []
        if not head:
            return False
        node = head
        while node:
            ans.append(node.val)
            node = node.next

        return True if ans == ans[::-1] else False