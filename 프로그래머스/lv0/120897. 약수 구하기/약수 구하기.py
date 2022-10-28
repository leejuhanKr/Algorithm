def solution(n):
    return [i for i in (*range(1,n//2+1),n) if n%i == 0]