def solution(i, j, k):
    return sum(str(w).count(str(k)) for w in range(i,j+1))