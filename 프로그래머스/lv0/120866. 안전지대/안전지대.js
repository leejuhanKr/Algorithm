function solution(board) {
    const n = board.length
    let res = 0
    for (let r = 0; r<n; r++) {
        for (let c = 0; c < n; c++) {
            if (board[r][c] === 1) continue
            let isSafe = true
            check: for (let dr of [-1, 0, 1]) {
                if (r+dr < 0 || r+dr >=n) continue
                for (let dc of [-1, 0, 1]) {
                    if (c+dc < 0 || c+dc >= n) continue
                    if (board[r+dr][c+dc] === 1) {
                        isSafe = false
                        break check
                    }
                }
            }
            if (isSafe) {
                res +=1
            }
        }
    }
    return res
}