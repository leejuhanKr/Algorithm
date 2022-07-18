import heapq
from sys import stdin

hq = []
heapq.heapify(hq)

for _ in range(int(input())):
    if a := int(stdin.readline()):
        heapq.heappush(hq,a)
    else:
        if hq:
            print(heapq.heappop(hq))
        else:
            print(0)