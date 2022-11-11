def solution(n, results):
    gh = [[0]*(n+1) for _ in range(n+1)]
    for a,b in results:
        gh[a][b] = 1
        
    res = [0]*(n+1)
    
    q = []
    visited = set()
    for start in range(1,n+1):
        q.append(start)
        while q:
            node = q.pop()
            if node in visited:
                continue
            visited.add(node)
            res[node]+=1
            for next, is_link in enumerate(gh[node]):
                if not is_link:
                    continue
                q.append(next)
        res[start] += len(visited)-1
        visited.clear()
        
    return sum((v == n) for v in res)
            
            
            
            
    