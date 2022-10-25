def solution(sides):
    a,b,c = sorted(sides)
    return 1 + ((a+b)<=c)