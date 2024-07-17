# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        arr = []
        
        # Traverse the linked list and store node values in the list
        temp = head
        while temp is not None:
            arr.append(temp.val)
            temp = temp.next
        
        # Sort the list containing node values
        arr.sort()
        
        # Reassign sorted values to the linked list nodes
        temp = head
        for value in arr:
            temp.val = value
            temp = temp.next
        
        # Return the head of the sorted linked list
        return head
