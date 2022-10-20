def solution(n):
    i = 0
    v = 0
    while i<n:
        v += 1
        if '3' not in str(v) and v%3:
            i+=1
    return v