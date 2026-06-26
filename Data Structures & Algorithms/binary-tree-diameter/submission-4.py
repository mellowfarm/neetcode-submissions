# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        curr_max = 0
        def depth(node):
            if node is None:
                return 0
            else:
                left = depth(node.left)
                right = depth(node.right)
                nonlocal curr_max 
                curr_max = max(curr_max, left + right)
                return 1 + max(left, right)
        
        depth(root)
        return curr_max
        
            
        