def solution(n):
    res = []
    while n != 1:
        for d in range(2,n+1):
            if n%d == 0:
                n = n//d
                if d not in res:
                    res.append(d)
                break
    return res