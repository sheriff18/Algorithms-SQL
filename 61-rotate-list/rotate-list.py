# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
        def rotateRight(self, head: ListNode, k: int) -> ListNode:
            if not head or not head.next or k == 0:
                return head

            
            old_tail = head
            length = 1
            while old_tail.next:
                old_tail = old_tail.next
                length += 1
            
            # Connect the tail to the head to make it circular
            old_tail.next = head

        
            k = k % length
            new_tail = head
            for _ in range(length - k - 1):
                
                new_tail = new_tail.next
            
            new_head = new_tail.next
            new_tail.next = None  # Break the circle

            return new_head
