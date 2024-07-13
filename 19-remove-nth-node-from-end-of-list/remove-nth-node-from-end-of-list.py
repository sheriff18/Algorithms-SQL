# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        right = head
        left = head

        for i in range(n):
            right = right.next
        
        if not right:
            return head.next

        while right.next:
            
            left = left.next
            right = right.next
        left.next = left.next.next

        return head



        