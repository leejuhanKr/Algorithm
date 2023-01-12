from sys import stdin

n = int(input())
A, B, C, D = [], [], [], []
for _ in range(n):
    for arr, v in zip((A, B, C, D), map(int, stdin.readline().split())):
        arr.append(v)

l = {}
for a in A:
    for b in B:
        key = -a - b
        l[key] = l.get(key, 0) + 1

print(sum(v for c in C for d in D if (v := l.get(c + d))))