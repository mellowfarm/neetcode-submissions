class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        parent = [i for i in range(n)]
        rank = [1] * n

        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return False
            if rank[root_y] <= rank[root_x]:
                parent[root_y] = root_x
                rank[root_x] += rank[root_y]
            else:
                parent[root_x] = root_y
                rank[root_y] += rank[root_x]
            return True
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) # path compression
            return parent[x]
        
        for edge in edges:
            x, y = edge[0], edge[1]
            if not union(x, y):
                return False
        
        return True
