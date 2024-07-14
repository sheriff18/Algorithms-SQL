# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        dummy = ListNode(next=head)
        
        # Initialize the current and previous pointers
        curr, prev = head, dummy
        
        while curr:
            if curr.val == val:
                # Skip the current node by linking previous node to next node
                prev.next = curr.next
            
            else:
                prev = curr
            
            curr = curr.next
        
        
        return dummy.next
        
        