class Solution:
    def solve(self, board: List[List[str]]) -> None:
        not_surrounded = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def dfs(i, j):
            if (i, j) in not_surrounded:
                return
            not_surrounded.add((i, j))
            for direction in directions:
                x, y = direction[0], direction[1]
                if 0 <= x+i < len(board) and 0 <= y+j < len(board[0]):
                    if board[x+i][y+j] == 'O':
                        dfs(x+i, y+j)
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if r == 0 or r == len(board)-1 or c == 0 or c == len(board[0])-1:
                    if board[r][c] == 'O':
                        dfs(r, c)
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O' and (r, c) not in not_surrounded:
                    board[r][c] = 'X'
                     