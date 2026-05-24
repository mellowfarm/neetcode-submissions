class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for i in range(len(board)):
            seen = set()
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in seen:
                    return False
                else:
                    seen.add(board[i][j])
        
        # check columns
        for i in range(len(board[0])):
            seen = set()
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in seen:
                    return False
                else:
                    seen.add(board[j][i])
        
        # check squares
        for box_row in range(3):
            for box_col in range(3):
                seen = set()    
                for i in range(box_row*3, box_row*3 + 3):
                    for j in range(box_col*3, box_col*3 + 3):
                        if board[i][j] == ".":
                            continue
                        elif board[i][j] in seen:
                            return False
                        else:
                            seen.add(board[i][j])
        
        return True

            