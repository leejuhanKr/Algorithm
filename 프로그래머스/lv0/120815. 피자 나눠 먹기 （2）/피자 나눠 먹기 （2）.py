def solution(n):
    g = gcd(n,6)
    return n//g

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a
