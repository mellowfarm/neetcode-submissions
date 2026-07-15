class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        queue = deque([])
        visited = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))
                    visited.add((r, c))
                    
        while queue:
            curr = queue.popleft()
            cr, cc, dist = curr[0], curr[1], curr[2]
            for direction in directions:
                dr, dc = direction[0], direction[1]
                nr, nc = dr+cr, dc+cc                    
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    if (nr, nc) not in visited and grid[nr][nc] == 2147483647:
                        queue.append((nr, nc, dist+1))
                        grid[nr][nc] = dist + 1
                        visited.add((nr, nc))


        

