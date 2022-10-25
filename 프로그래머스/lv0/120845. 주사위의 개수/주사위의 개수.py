def solution(box, n):
    [a,b,c] = map(lambda x: x//n, box)
    return a*b*c
