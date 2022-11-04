def solution(rows, cols, qs):
    b = [[*range(i,i+cols)] for i in range(1,rows*cols,cols)]
    return [turn(b,q) for q in qs]

def turn(b, q):
    pos = [*gen_pos(q)]
    val = [b[r][c] for r,c in pos[1:]+[pos[0]]]
    for (r,c),v in zip(pos,val):
        b[r][c] = v
    return min(val)

def gen_pos(q):
    r1,c1,r2,c2 = map(lambda x: x-1, q)
    yield from ((r,c1) for r in range(r1,r2))
    yield from ((r2,c) for c in range(c1,c2))        
    yield from ((r,c2) for r in range(r2,r1,-1))
    yield from ((r1,c) for c in range(c2,c1,-1))
