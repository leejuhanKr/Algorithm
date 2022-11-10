from math import gcd

def check(arrA, arrB):
    c1 = arrA[0]
    for n in arrA:
        if (c1:=gcd(c1, n)) == 1:
            return 0
    for c in range(c1,1,-1):
        if c1%c==0 and all(n%c for n in arrB):
            return c
    return 0

def solution(arrayA, arrayB):
    return max(check(arrayB, arrayA), check(arrayA, arrayB))
            
        
    
