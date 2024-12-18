# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        t1 = head
        arr[k-1],arr[-k] = arr[-k],arr[k-1]
        while t1:
            t1.val = arr.pop(0)
            t1 = t1.next
        return head