import math
def solution(n, k):
    res = []
    s = [*range(1,n+1)]
    k-=1
    for i in range(n):
        q,k = divmod(k,math.factorial(n-1-i))
        res.append(s.pop(q))
    return res