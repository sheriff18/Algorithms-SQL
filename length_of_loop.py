https://www.geeksforgeeks.org/problems/find-length-of-loop/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=find-length-of-loop

#User function Template for python3

'''
Structure of node

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''

#Function to find the length of a loop in the linked list.
def countNodesinLoop(head):
    def detectLoop(head):
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return None
    
    # Detect loop
    meeting_point = detectLoop(head)
    if not meeting_point:
        return 0

    # Count the number of nodes in the loop
    loop_length = 1
    current = meeting_point.next
    while current != meeting_point:
        current = current.next
        loop_length += 1
    
    return loop_length
    
        
            
    
    
   
    

