class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]

        def union(x, y):
            root_x = find(x) # x's parent
            root_y = find(y) # y's parent
            if root_x != root_y:
                parent[root_y] = root_x 
         
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        for edge in edges:
            x, y = edge[0], edge[1]
            union(x, y)

        seen = set()
        for p in parent:
            root = find(p)
            if root not in seen:
                seen.add(root)
        
        return len(seen)