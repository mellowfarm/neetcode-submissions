# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        if root is None:
            return []
        queue = deque([])
        res = []
        queue.append((root, 0))

        while queue:
            node, level = queue.popleft()
            if queue:
                next_level = queue[0][1]
                if next_level != level:
                    res.append(node.val)
            else:
                res.append(node.val)
            if node.left is not None:
                queue.append((node.left, level+1))
            if node.right is not None:
                queue.append((node.right, level+1))
        
        return res

        
        
        
