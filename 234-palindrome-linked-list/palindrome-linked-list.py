# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        new_head = self.reverseLinkedList(head.next)
        head.next.next = head
        head.next = None
        return new_head
        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True

        # Find the end of the first half and reverse the second half
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        second_half_start = self.reverseLinkedList(slow)
        first_half_start = head

        # Check whether or not there's a palindrome
        result = True
        first = first_half_start
        second = second_half_start

        while second:
            if first.val != second.val:
                result = False
                break
            first = first.next
            second = second.next

      
        slow.next = self.reverseLinkedList(second_half_start)

        return result
