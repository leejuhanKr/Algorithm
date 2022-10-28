from math import factorial as f
def solution(n, m):
    return f(n)/f(n-m)/f(m)

