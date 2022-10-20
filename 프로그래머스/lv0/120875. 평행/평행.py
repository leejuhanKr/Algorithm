def solution(dots):
    combs = [(0,1,2,3), (0,2,1,3), (0,3,1,2)]
    return +any([is_parallel(*(dots[i] for i in comb)) for comb in combs])
    
def is_parallel(d1,d2,d3,d4):
    return (d2[0]-d1[0])*(d4[1]-d3[1]) == (d2[1]-d1[1])*(d4[0]-d3[0])
    
    