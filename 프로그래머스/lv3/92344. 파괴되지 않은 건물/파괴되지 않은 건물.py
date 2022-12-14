def solution(board, skill):
    _b = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    for t,r1,c1,r2,c2,d in skill:
        if t==2:
            d*=-1
        _b[r1][c1] -= d
        _b[r1][c2+1] += d
        _b[r2+1][c1] += d
        _b[r2+1][c2+1] -= d
    for c in range(len(board[0])):
        for r in range(1,len(board)):
            _b[r][c] += _b[r-1][c]
    for r in range(len(board)):
        for c in range(1,len(board[0])):
            _b[r][c] += _b[r][c-1]
    res = 0
    for r in range(len(board)):
        for c in range(len(board[0])):
            if _b[r][c]+board[r][c] > 0:
                res+=1
            board[r][c] += _b[r][c]
    return res