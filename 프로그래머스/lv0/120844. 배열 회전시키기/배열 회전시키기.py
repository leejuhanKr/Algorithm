def solution(n, d):
    return [n[1:]+[n[0]],[n[-1],*n[:-1]]][d[0]=='r']