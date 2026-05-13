class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        graph = grid 
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        count = 0

        def dfs(i, j):
            graph[i][j] = "0"
            for dr, dc in directions:
                nr, nc = i+dr, j+dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    if graph[nr][nc] == "1":
                        dfs(nr, nc)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
        
        return count