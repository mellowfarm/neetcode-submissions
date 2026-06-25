# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        depth = 0
        if root is None:
            return depth
        queue = deque([(root, depth+1)])
        while queue:
            node, curr_depth = queue.popleft()
            if node is None:
                depth = curr_depth - 1
                continue
            queue.append((node.left, curr_depth+1))
            queue.append((node.right, curr_depth+1))
        
        return depth
        


