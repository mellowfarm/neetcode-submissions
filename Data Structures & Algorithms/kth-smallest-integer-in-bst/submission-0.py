# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # find size of tree
        def size(root):
            if root is None:
                return 0
            else:
                return 1 + size(root.left) + size(root.right)
        
        root_idx = size(root.left) + 1
        if root_idx == k:
            return root.val
        else:
            if k < root_idx:
                return self.kthSmallest(root.left, k)
            else:
                return self.kthSmallest(root.right, k-root_idx)
        