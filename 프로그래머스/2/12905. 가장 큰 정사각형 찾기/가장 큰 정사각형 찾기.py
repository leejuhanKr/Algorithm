def solution(board):
    res = any(any(val for val in row) for row in board)
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if v:= board[i][j]:
                v = min(board[i-1][j],board[i][j-1],board[i-1][j-1])+1
                board[i][j] = v
                res = max(res, v)
                
    return res**2
                        
