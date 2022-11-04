from collections import namedtuple
import heapq as hq

Node = namedtuple('Node', ['weight', 'name'])
inf = 10e9

def solution(N, road, K):
    gh = [[inf]*(N+1) for _ in range(N+1)]
    for s,e,w in road:
        gh[s][e] = gh[e][s] = min(gh[s][e],w)
        
    dist = [inf]*(N+1)
    dist[1] = 0
    
    q = [Node(dist[1],1)]
    while q:
        node = hq.heappop(q)
        for name, weight in enumerate(gh[node.name]):
            if dist[name] > dist[node.name] + weight:
                dist[name] = dist[node.name] + weight
                hq.heappush(q,Node(dist[name], name))

    return sum(w<=K for w in dist)
    