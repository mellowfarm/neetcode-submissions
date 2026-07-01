# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        queue = deque([])
        res = []
        if root is not None:
            queue.append((root, 0))
        else:
            return res
        
        curr_depth = 0
        curr_list = []
        while queue:
            node, depth = queue.popleft()
            if node.left is not None:
                queue.append((node.left, depth+1)) 
            if node.right is not None:
                queue.append((node.right, depth+1))
            if depth == curr_depth:
                curr_list.append(node.val)
            else:
                res.append(curr_list)
                curr_depth = depth
                curr_list = [node.val]
        res.append(curr_list)
        return res

            