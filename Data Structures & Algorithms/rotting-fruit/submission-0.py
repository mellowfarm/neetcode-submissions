class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])
        visited = set()
        num_fruits = 0
        total_time = 0

        # find rotting fruit
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    num_fruits += 1
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                    visited.add((r, c))
        
        # bfs
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            curr = queue.popleft()
            cr, cc, curr_time = curr[0], curr[1], curr[2]
            for direction in directions:
                dr, dc = direction[0], direction[1]
                nr, nc = cr+dr, cc+dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    if grid[nr][nc] == 1 and (nr, nc) not in visited:
                        queue.append((nr, nc, curr_time+1))
                        visited.add((nr, nc))
            total_time = curr_time
        
        if len(visited) == num_fruits:
            return total_time
        else:
            return -1
            
                



        


        
        
                    



                
            
            

