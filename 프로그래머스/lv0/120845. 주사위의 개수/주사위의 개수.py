from functools import reduce
def solution(box, n):
    return reduce(lambda acc, cur: acc*(cur//n), box, 1)
