# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(node, after):
            # Reverse the nodes between `node` and `after`
            prev, cur = None, node
            while cur != after:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev  # New head of the reversed segment

        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = head
        
        while cur:
            tail = cur
            for _ in range(k):
                if not tail:
                    return dummy.next
                tail = tail.next
            
            next_group = tail
            new_head = reverse(cur, next_group)
            
            pre.next = new_head
            cur.next = next_group
            
            pre = cur
            cur = next_group
        
        return dummy.next

            