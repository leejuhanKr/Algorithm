import sys
sys.setrecursionlimit(15000)

def solution(a, b, n):
    q,r = divmod(n,a)
    return q*b + solution(a,b,q*b+r) if q else 0

    
