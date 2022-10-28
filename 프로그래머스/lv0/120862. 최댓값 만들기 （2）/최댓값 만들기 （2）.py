def solution(n):
    n.sort()
    return max(n[0]*n[1],n[-2]*n[-1])