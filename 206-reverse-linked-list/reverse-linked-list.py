# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr,prev = head, None

        while curr:
            new_node = curr.next
            curr.next = prev
            prev = curr
            curr = new_node
        return prev
        