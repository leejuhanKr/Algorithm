from sys import stdin
import heapq

N, M = map(int, input().split())
lst = list(map(lambda x: x.rstrip(), stdin.readlines()))

a = lst[:N]
b = lst[N:N+M+1]

heapq.heapify(a)
heapq.heapify(b)

res = []
while (a and b):
    if a[0] == b[0]:
        res.append(a[0])
        heapq.heappop(a)
        heapq.heappop(b)
    elif a[0]<b[0]:
        heapq.heappop(a)
    else:
        heapq.heappop(b)

print(len(res))
print("\n".join(res))