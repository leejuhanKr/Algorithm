def solution(dots):
    combs = [(0,1,2,3), (0,2,1,3), (0,3,1,2)]

    return +any([is_parallel(dots,comb) for comb in combs])
    
def is_parallel(dots,foo):
    d = [dots[i] for i in foo]

    # m1 = (d[1][1]-d[0][1])/(d[1][0]-d[0][0])
    # m2 = (d[3][1]-d[2][1])/(d[3][0]-d[2][0])

    return m(d[0],d[1]) == m(d[2],d[3])

def m(d1,d2):
    dx = d2[0]-d1[0]
    if not dx:
        return 'inf'
    else:
        return (d2[1]-d1[1])/dx
    
    