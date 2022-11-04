from collections import namedtuple
import heapq as hq

Node = namedtuple('Node', ['weight', 'name'])

def solution(N, road, K):
    inf = 10e9
    gh = [[inf]*(N+1) for _ in range(N+1)]
    for s,e,w in road:
        w = min(gh[s][e],w)
        gh[s][e] = gh[e][s] = w
        
    dist = [inf]*(N+1)
    dist[1] = 0
    
    q = []
    node = Node(dist[1],1)
    hq.heappush(q,node)
    
    while q:
        node = hq.heappop(q)
        for name, weight in enumerate(gh[node.name]):
            if dist[name] < dist[node.name] + weight:
                continue
            dist[name] = dist[node.name] + weight
            hq.heappush(q,Node(weight, name))

    return sum(w<=K for w in dist)
    