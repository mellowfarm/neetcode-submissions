class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            seen = set()
            for col in range(len(board[0])):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])
        
        for col in range(len(board[0])):
            seen = set()
            for row in range(len(board)):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])
        
        for row in range(3):
            for col in range(3):
                seen = set()
                for i in range(row*3, row*3 + 3):
                    for j in range(col*3, col*3 + 3):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in seen:
                            return False
                        seen.add(board[i][j])
        
        return True
