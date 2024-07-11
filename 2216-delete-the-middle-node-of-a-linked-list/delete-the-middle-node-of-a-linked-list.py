class Solution:

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return None  # Handle empty or single-node list

        # Single-pass deletion with two pointers (fast and slow)
        fast, slow = head, head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # # Handle lists with even number of nodes
        # if fast:  # If fast reaches the end (even number of nodes)
        #     return head

        # Remove middle node considering duplicates (modify prev's next pointer)
        if prev:
            prev.next = slow.next

        return head
