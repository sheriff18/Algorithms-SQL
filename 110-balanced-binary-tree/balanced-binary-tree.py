# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Helper function to check the height of the tree.
        def height(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            # If any subtree is unbalanced, return -1
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1

            # Return the height of the subtree
            return 1 + max(left_height, right_height)

        # If height returns -1, the tree is unbalanced
        return height(root) != -1
