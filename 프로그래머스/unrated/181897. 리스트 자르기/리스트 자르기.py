def solution(n, slicer, num_list):
    [a,b,c] = slicer
    if n == 1:
        _slice = slice(0,b+1)
    elif n==2:
        _slice = slice(a,None)
    elif n==3:
        _slice = slice(a,b+1)
    elif n==4:
        _slice = slice(a,b+1,c)
        
    return num_list[_slice]