def solution(n, costs):
    res = 0
    costs.sort(key = lambda x: x[2], reverse=True)
    parents = [i for i in range(n)]
    
    while costs:
        a,b,cost = costs.pop()
        if parents[a] == parents[b]:
            continue
        res += cost
        root = parents[b]
        for i in range(n):
            if parents[i] == root:
                parents[i] = parents[a]
        if len(set(parents)) == 1:
            break
            
    return res
        
    