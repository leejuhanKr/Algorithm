from collections import deque
        
def solution(n, lh):
    gh = [set() for _ in range(n+1)]
    for a,b in lh:
        gh[a].add(b)
        gh[b].add(a)

    visited = set()
    stack = []
    q = deque([(1,0)])
    gh[1].add(0)
    gh[0].add(1)
    while q:
        node, parent = q.popleft()
        if node in visited:
            continue
        
        visited.add(node)
        stack.append((node,parent))
        gh[node].remove(parent)
        for next in gh[node]:
            q.append((next, node))

    on = 0
    while stack:
        node, parent = stack.pop()
        childs = gh[node]

        if childs:
            on+=1
            gh[parent].remove(node)
    return on          


    
            
        



            
            
    

            
    