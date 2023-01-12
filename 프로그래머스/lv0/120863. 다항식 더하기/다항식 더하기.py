def solution(s):
    p = [0,0]

    for w in s.split(' + '):
        if w.endswith('x'):
            p[0] += int(p0) if (p0:=w.rstrip('x')) else 1
        else:
            p[1] += int(w)
            
    res = []
    if p0:=p[0]:
        res.append(f'{str(p0)}x' if p0 != 1 else 'x')
    if p1:=p[1]:
        res.append(str(p1))

    return ' + '.join(res)
        
        
    