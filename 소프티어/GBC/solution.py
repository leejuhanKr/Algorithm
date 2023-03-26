from sys import stdin
from itertools import repeat


def preprocess_input():
    n, m = map(int, stdin.readline().split())
    limits = []
    for _ in range(n):
        limits.append(tuple(map(int, stdin.readline().split())))
    testcases = []
    for _ in range(m):
        testcases.append(tuple(map(int, stdin.readline().split())))
    return limits, testcases


def generate_speed(speed_info):
    for _len, speed in speed_info:
        yield from repeat(speed, _len)


def solution():
    limits, testcases = map(generate_speed, preprocess_input())
    return max(
        *(speed - limit_speed for limit_speed, speed in zip(limits, testcases)), 0
    )


print(solution())
