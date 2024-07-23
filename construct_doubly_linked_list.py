

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''
class Solution:
    def constructDLL(self, arr):
        n = len(arr)
        head = Node(arr[0])
        current = head
        
        for i in range(1,n):
            new_node = Node(arr[i])
            current.next = new_node
            new_node.prev = current
            current = new_node
            
        return head
        
