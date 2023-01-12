import heapq as hq
def solution(k, score):
    res = []
    q = []
    for s in score[:k]:
        hq.heappush(q, s)
        res.append(q[0])
    for s in score[k:]:
        if q[0] < s:
            hq.heapreplace(q,s)
        res.append(q[0])
    return res
        
    