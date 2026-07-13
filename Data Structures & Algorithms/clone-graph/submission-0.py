"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        old_to_new = {}
        queue = deque([node])
        copy = None

        while queue:
            curr = queue.popleft()
            val, neighbors = curr.val, curr.neighbors
            if copy is None:
                new = Node(val, [])
                copy = new
                old_to_new[curr] = new
            for neighbor in curr.neighbors:
                if neighbor in old_to_new:
                    old_to_new[curr].neighbors.append(old_to_new[neighbor])
                    continue
                new_neighbor = Node(neighbor.val, [])
                old_to_new[curr].neighbors.append(new_neighbor)
                old_to_new[neighbor] = new_neighbor
                queue.append(neighbor)
        
        return copy

            

            
            
            