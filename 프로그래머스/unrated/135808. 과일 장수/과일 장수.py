def solution(k, m, score):
    return sum(sorted(score)[len(score)%m::m])*m
