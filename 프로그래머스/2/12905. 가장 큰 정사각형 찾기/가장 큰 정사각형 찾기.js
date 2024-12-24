// def solution(board):
//    res = any(any(val for val in row) for row in board)
//    for i in range(1,len(board)):
//        for j in range(1,len(board[0])):
//            if v:= board[i][j]:
//                v = min(board[i-1][j],board[i][j-1],board[i-1][j-1])+1
//                board[i][j] = v
//                res = max(res, v)
//                
//    return res**2

const solution = (board) => {
    let res = 0;
    for (let i=0; i<board.length; i++) {
        if (board[i][0] || board[0][i]) {
            res = 1;
            break
        }
    }
    for (let x=1; x<board.length; x++) {
        for (let y=1; y<board[0].length; y++) {
            if (!board[x][y]) continue;
            board[x][y] = Math.min(
                ...[[1,0],[0,1],[1,1]].map(([dx,dy])=>board[x-dx][y-dy])
            ) + 1
            res = board[x][y] > res ? board[x][y] : res
        }
    }
    return res ** 2
}
                        