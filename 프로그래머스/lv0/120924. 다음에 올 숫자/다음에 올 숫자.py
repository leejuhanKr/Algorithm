def solution(common):
    [*_,a,b,c] = common
    return c+b-a if b-a == c-b else c*(b//a)