# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def builder(preorder, inorder):
            if not preorder or not inorder:
                return None
            root_val = preorder[0]
            root = TreeNode(root_val, None, None)

            left_inorder = None
            right_inorder = None
            left_preorder = None
            right_preorder = None
            for i, val in enumerate(inorder):
                if val == root_val:
                    left_inorder = inorder[:i]
                    right_inorder = inorder[i+1:]
                    left_preorder = preorder[1:len(left_inorder)+1]
                    right_preorder = preorder[len(left_inorder)+1:]
                    break
            
            root.left = builder(left_preorder, left_inorder)
            root.right = builder(right_preorder, right_inorder)
            return root
        
        return builder(preorder, inorder)

            
            
            
            
                
                