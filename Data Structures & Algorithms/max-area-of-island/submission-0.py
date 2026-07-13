class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        graph = grid
        max_area = 0
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]

        self.curr_size = 0
        def dfs(i, j):
            graph[i][j] = 0
            self.curr_size += 1
            for direction in directions:
                x, y = direction[0], direction[1]
                if 0 <= i+x < len(graph) and 0 <= j+y < len(graph[0]):
                    if graph[i+x][j+y] == 1:
                        dfs(i+x, j+y)
        
        for r in range(len(graph)):
            for c in range(len(graph[0])):
                if graph[r][c] == 1:
                    dfs(r, c)
                    max_area = max(self.curr_size, max_area)
                    self.curr_size = 0
        
        return max_area
        

        