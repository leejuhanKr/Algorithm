def solution(a, b):
    b //= gcd(a,b)
    return [2,1][gcd(2**10 * 5**5, b)==b]

def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a
