# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam = 0  # Initialize diameter as 0
        
        # Helper function to calculate the height and update the diameter
        def height(node: Optional[TreeNode]) -> int:
            nonlocal diam  # Declare diam as nonlocal to modify it inside the helper function
            
            if node is None:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            # Update the diameter if the path through the current node is larger
            curr_diameter = left_height + right_height
            diam = max(diam, curr_diameter)

            # Return the height of the current node
            return 1 + max(left_height, right_height)

        height(root)  # Call the height function to update the diameter
        return diam  # Return the final diameter
