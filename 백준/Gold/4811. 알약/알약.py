from sys import stdin, setrecursionlimit

setrecursionlimit(15000)


def memoization(func):
    _dict = {}

    def memoized(*args):
        if args not in _dict:
            _dict[args] = func(*args)
        return _dict[args]

    return memoized


@memoization
def g(w, h):
    if h > w:
        return 0
    if h == 0:
        return 1
    return g(w - 1, h) + g(w, h - 1)


def f(n):
    return g(n, n)


while N := int(stdin.readline()):
    print(f(N))
