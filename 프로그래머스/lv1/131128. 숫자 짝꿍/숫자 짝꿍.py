def solution(X, Y):
    _map = [[0,0] for _ in range(10)]
    for i,j in zip((X,Y),(0,1)):
        for k in map(int,i):
            _map[k][j] += 1

    res = "".join(reversed([str(i)*min(vs) for i,vs in enumerate(_map)]))
    return '-1' if res == '' else '0' if res.startswith('0') else res

        
