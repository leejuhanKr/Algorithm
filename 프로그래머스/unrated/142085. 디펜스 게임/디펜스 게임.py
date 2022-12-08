import heapq as hq
def solution(n, k, enemy):
    q = enemy[:k]
    hq.heapify(q)
    for idx in range(k,len(enemy)):
        n -= hq.heappushpop(q,enemy[idx])
        if n < 0:
            return idx
    return len(enemy)