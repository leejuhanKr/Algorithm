import heapq as hq
inf = 10e9

def solution(n, roads, sources, destination):
    gh = [[] for _ in range(n+1)]
    for a,b, in roads:
        gh[a].append(b)
        gh[b].append(a)
        
    dist = Dijkstra(n, gh, destination)
    
    return [d if (d:=dist[i])!=inf else -1 for i in sources]

def Dijkstra(n, gh, st):
    dist = [inf] * (n+1)
    dist[st]=0
    
    q =[(dist[st], st)]
    hq.heapify(q)
    
    while q:
        d, node = hq.heappop(q)
        for next in gh[node]:
            new = d + 1
            if new < dist[next]:
                dist[next] = new
                q.append((new, next))
    return dist
    