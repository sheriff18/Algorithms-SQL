from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        def findMid(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        mid = findMid(head)
        right = mid.next
        mid.next = None
        
        left = self.sortList(head)
        right = self.sortList(right)
        
        def merge_sort(left, right):
            dummy = ListNode(0)
            curr = dummy
            while left and right:
                if left.val < right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                curr = curr.next
            
            if left:
                curr.next = left
            if right:
                curr.next = right
                
            return dummy.next

        return merge_sort(left, right)
