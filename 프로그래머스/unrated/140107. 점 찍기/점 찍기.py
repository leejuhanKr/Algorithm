def solution(k, d):
    return sum(((d**2-y**2)**0.5)//k+1 for y in range(0,d+1,k))
