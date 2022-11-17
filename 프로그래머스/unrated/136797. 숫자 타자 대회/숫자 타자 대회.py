def solution(numbers):
    key = {0:(3,1), **{n:divmod(n-1,3) for n in range(1,10)}}

    ws = [[1]*10 for _ in range(10)]
    for i in range(10):
        x_i, y_i = key[i]
        for j in range(i):
            x_j, y_j = key[j]
            dx , dy = map(abs, (x_i-x_j, y_i-y_j))
            ws[j][i] = ws[i][j] = max(dx,dy)+sum((dx,dy))
    dp = [(6,0)]
    p = 4
    for n in numbers:
        n = int(n)
        d = {}
        for pp,w in dp:
            if p != n:
                d[p] = min(d.get(p,10e9),w+ws[pp][n])
            if pp != n:
                d[pp] = min(d.get(pp,10e9),w+ws[p][n])
        p=n
        dp = [(k,v) for k,v in d.items()]

    return min((w for _,w in dp))

            