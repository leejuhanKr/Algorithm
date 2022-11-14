def solution(tickets):
    tickets.sort()
    pos = {'ICN': 0}
    for s,e in tickets:
        for p in (s,e):
            if p not in pos:
                pos[p] = len(pos)

    sop = {v:k for k,v in pos.items()}
    gh = [[] for _ in pos]
    for s,e in tickets:
        gh[pos[s]].append([pos[e],1])
    
    visited = [0, *(-1 for _ in tickets)]

    res = 0
    def back(tmp):
        nonlocal res
        if res:
            return
        if tmp == len(visited):
            res = visited[:]
            return
            
        for t_info in gh[visited[tmp-1]]:
            dist, isAble = t_info
            if not isAble:
                continue
            visited[tmp] = dist
            t_info[1] = 0
            back(tmp+1)
            t_info[1] = 1
    back(1)     
    return [sop[i] for i in res]