from itertools import islice
from sys import maxsize, stdin


def preprocess_input():
    M, N, K = map(int, stdin.readline().split())
    key = tuple(int(i) for i in stdin.readline().split())
    order = [int(i) for i in stdin.readline().split()]
    return M, N, K, key, order


def pairwise(iterable, _len):
    yield from zip(*(islice(iterable, i, maxsize) for i in range(_len)))


def solution():
    M, N, K, secret_key, order = preprocess_input()
    for key in pairwise(order, M):
        if secret_key == key:
            return "secret"
    return "normal"


answer = solution()
print(answer)
