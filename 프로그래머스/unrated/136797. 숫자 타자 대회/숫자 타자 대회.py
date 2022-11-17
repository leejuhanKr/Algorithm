def solution(numbers):
    key = {0:(3,1), **{n:divmod(n-1,3) for n in range(1,10)}}

    ws = [[1]*10 for _ in range(10)]
    for i in range(10):
        x_i, y_i = key[i]
        for j in range(i):
            x_j, y_j = key[j]
            dx , dy = map(abs, (x_i-x_j, y_i-y_j))
            ws[j][i] = ws[i][j] = max(dx,dy)+sum((dx,dy))
    dp = [(4,6,0)]
    for n in numbers:
        n = int(n)
        d = {}
        for l,r,w in dp:
            for nl,nr,dw in [(n,r,ws[l][n]), (l,n,ws[r][n])]:
                if nl==nr:
                    continue
                d[(nl,nr)] = min(d.get((nl,nr),10e9),w+dw)
        dp = [(*k,v) for k,v in d.items()]
    ans = 10e9
    for _,_,w in dp:
        ans = min(ans,w)
    return ans

            