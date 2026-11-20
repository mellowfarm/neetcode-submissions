class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0

        def dfs(grid, x, y):
            directions = [(0,1), (1,0), (-1, 0), (0, -1)]
            stack = [(x, y)]
            while stack:
                curr_x, curr_y = stack.pop()
                for d in directions:
                    n_x, n_y = curr_x + d[0], curr_y + d[1]
                    if 0 <= n_x < len(grid) and 0 <= n_y < len(grid[0]):
                        if grid[n_x][n_y] == "1":
                            stack.append((n_x, n_y))
                grid[curr_x][curr_y] = "0"

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    dfs(grid, x, y)
                    num_islands += 1
        
        return num_islands