# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_val = p.val
        q_val = q.val
        root_val = root.val
        if p_val < root_val and q_val < root_val:
            # must be on the left
            return self.lowestCommonAncestor(root.left, p, q)
        elif p_val > root_val and q_val > root_val:
            # must be on the right
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
