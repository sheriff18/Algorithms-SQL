# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            print("no cycle")
            return None

        temp = head
        hm = {}
        while temp:
            if temp in hm.keys():
                return temp
            else:
                hm[temp] = 1
            temp = temp.next

        return None
        