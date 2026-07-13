class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        pacific = set()
        atlantic = set()

        def dfs_pacific(i, j):
            if (i, j) in pacific:
                return
            pacific.add((i, j))

            for direction in directions:
                x, y = direction[0], direction[1]
                if 0 <= x+i < len(heights) and 0 <= y+j < len(heights[0]):
                    if heights[x+i][y+j] >= heights[i][j]:
                        dfs_pacific(x+i, y+j)
        
        def dfs_atlantic(i, j):
            if (i, j) in atlantic:
                return
            atlantic.add((i, j))

            for direction in directions:
                x, y = direction[0], direction[1]
                if 0 <= x+i < len(heights) and 0 <= y+j < len(heights[0]):
                    if heights[x+i][y+j] >= heights[i][j]:
                        dfs_atlantic(x+i, y+j)
            

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                # borders only
                if r == 0 or c == 0:
                    dfs_pacific(r, c)
                if r == len(heights)-1 or c == len(heights[0])-1:
                    dfs_atlantic(r, c)
        
        result = pacific & atlantic
        both = []
        for param in result:
            i, j = param[0], param[1]
            both.append([i, j])
        
        return both
        

                