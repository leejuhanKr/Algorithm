def solution(m, n, board):
    b = [list(reversed(cols)) for cols in zip(*board)]
    changed = True
    while changed:
        changed = False
        check = [[1]*len(s) for s in b]
        for r in range(1, len(b)):
            for c in range(1, len(b[r])):
                if c < len(b[r-1]):
                    ps = [(r,c), (r-1,c), (r,c-1), (r-1,c-1)]
                    if len(set([b[x][y] for x,y in ps])) == 1:
                        for x,y in ps:
                            check[x][y] = 0
                            changed = True

        b = [[v for v,cond in zip(r1,r2) if cond] for r1,r2 in zip(b,check)]
        
    return m*n - sum(map(len, b))