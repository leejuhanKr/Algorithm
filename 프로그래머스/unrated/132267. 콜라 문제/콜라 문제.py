import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)
def solution(a, b, n):
    q,r = divmod(n,a)
    if q==0:
        return 0
    return q*b + solution(a,b,q*b+r) 

    
