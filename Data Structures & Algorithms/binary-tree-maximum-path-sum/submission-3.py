# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.curr_max = float("-inf")
        def helper(root):
            if root is None:
                return 0
            val = root.val
            left_max = max(helper(root.left), 0)
            right_max = max(helper(root.right), 0)
            self.curr_max = max(self.curr_max, val+left_max+right_max)
            return val + max(left_max, right_max) # path cannot branch to both directions

        helper(root)
        return self.curr_max

            
            