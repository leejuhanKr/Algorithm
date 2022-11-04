def solution(rows, cols, qs):
    b = [[*range(1+i*cols,1+i*cols+cols)] for i in range(rows)]
    return [turn(b,q) for q in qs]

def turn(b, q):
    r1,c1,r2,c2 = map(lambda x: x-1, q)
    p_r,p_c = r1, c1+1
    _min = b[p_r][p_c]
    c = c1
    for r in range(r1,r2):
        _min = min(_min,b[r][c])
        b[r][c], b[p_r][p_c] = b[p_r][p_c], b[r][c]
        p_r,p_c = r,c
    r = r2
    for c in range(c1,c2):
        _min = min(_min,b[r][c])
        b[r][c], b[p_r][p_c] = b[p_r][p_c], b[r][c]
        p_r,p_c = r,c
    c = c2
    for r in range(r2,r1,-1):
        _min = min(_min,b[r][c])
        b[r][c], b[p_r][p_c] = b[p_r][p_c], b[r][c]
        p_r,p_c = r,c
    r = r1
    for c in range(c2,c1+1,-1):
        _min = min(_min,b[r][c])
        b[r][c], b[p_r][p_c] = b[p_r][p_c], b[r][c]
        p_r,p_c = r,c
    return _min
    
    
    