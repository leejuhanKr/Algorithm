def solution(n, l, r):
    return sum(i=='1' for i in foo(n, l-1, r))

def foo(n,l,r):
    if n == 0:
        return '1'
    ql, rl = divmod(l,5)
    qr, rr = divmod(r,5)
    
    prev = foo(n-1, ql, qr+1)
    res = ''
    for char in prev:
        if char == '1':
            res += '11011'
        else:
            res += '00000'
    return res[rl: rl+r-l]
    