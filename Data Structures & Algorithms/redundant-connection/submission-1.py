class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)] # ignore index 0

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y: # same parent alrd unioned
                return False
            parent[root_y] = root_x
            return True

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for edge in edges:
            x, y = edge[0], edge[1]
            if not union(x, y):
                return edge
        
            