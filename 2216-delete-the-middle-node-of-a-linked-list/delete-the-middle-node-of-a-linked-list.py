class Solution:

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return None  # Handle empty or single-node list

        # Single-pass deletion with two pointers (fast and slow)
        fast, slow,prev = head, head, None
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = slow.next
        return head
        
