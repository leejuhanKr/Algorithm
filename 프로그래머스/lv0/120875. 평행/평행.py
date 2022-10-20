def solution(dots):
    combs = [(0,1,2,3), (0,2,1,3), (0,3,1,2)]
    return +any([is_parallel([dots[i] for i in comb]) for comb in combs])
    
def is_parallel(d):
    return (d[1][0]-d[0][0])*(d[3][1]-d[2][1]) == (d[1][1]-d[0][1])*(d[3][0]-d[2][0])
    
    