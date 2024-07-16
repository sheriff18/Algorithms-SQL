# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_meeting_point(head):
            fast = slow = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
                if slow == fast:
                    return slow
            return None
        
        meeting_point = get_meeting_point(head)
        if not meeting_point:
            return None

        slow = head
        fast = meeting_point

        while slow != fast:
            fast = fast.next
            slow = slow.next
        return fast



