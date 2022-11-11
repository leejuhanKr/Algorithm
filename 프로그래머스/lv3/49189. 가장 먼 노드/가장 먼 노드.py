import heapq as hq

inf = 10e9

def solution(n, edge):
    gh = [[] for _ in range(n+1)]
    for a,b in edge:
        gh[a].append(b)
        gh[b].append(a)

    dist = [inf] * (n+1)
    
    start = 1
    dist[start] = 0
    q = [(dist[start],start)]
    
    while q:
        d, node = hq.heappop(q)
        if d < inf:
            for next in gh[node]:
                if dist[next] < inf:
                    continue
                dist[next] = d+1
                hq.heappush(q,(dist[next], next))

    max_dist = max(dist[1:])

    return sum(i ==max_dist for i in dist)
    
    
    