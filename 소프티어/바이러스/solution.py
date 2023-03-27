from sys import stdin
from itertools import repeat
from functools import reduce


def pre_div(func):
    div_const = 1_000_000_007

    def _wrapper(*args, **kwargs):
        return func(*args, **kwargs) % div_const

    return _wrapper


@pre_div
def _mul(a, b):
    return a * b


def solution():
    k, p, n = map(int, stdin.readline().split())
    return reduce(_mul, repeat(p, n), k)


print(solution())
