def solution(hp):
    res = 0
    for i in [5,3,1]:
        r,q = divmod(hp,i)
        res+=r
        hp=q
    return res