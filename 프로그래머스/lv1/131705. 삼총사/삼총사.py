from itertools import combinations

def solution(number):
    return sum(sum(n) == 0 for n in combinations(number,3))