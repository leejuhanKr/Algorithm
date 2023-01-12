def solution(m, n1, n2):
    return m[:n1]+m[n2]+m[n1+1:n2]+m[n1]+m[n2+1:]