# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val:i for i, val in enumerate(inorder)}

        def builder(left_idx, right_idx, pre_idx):
            if left_idx > right_idx:
                return None
            root_val = preorder[pre_idx]
            root = TreeNode(root_val, None, None)

            mid = idx_map[root_val]
            root.left = builder(left_idx, mid-1, pre_idx + 1)
            root.right = builder(mid+1, right_idx, pre_idx + (mid - left_idx) + 1)
            return root
        
        return builder(0, len(inorder)-1, 0)

            
            
            
            
                
                