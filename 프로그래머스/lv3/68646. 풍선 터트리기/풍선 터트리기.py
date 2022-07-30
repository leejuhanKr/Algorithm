import heapq

def solution(a):
    if len(a) <= 2:
        return len(a)
    
    q = [(v,i) for i,v in enumerate(a)]
    heapq.heapify(q)
    
    res = 2
    
    _,i_l = heapq.heappop(q)
    _,i_r = heapq.heappop(q)
    [i_l, i_r] = sorted((i_l, i_r))
    
    while (i_l != 0 or i_r != len(a)-1):
        _,i = heapq.heappop(q)

        if i < i_l:
            i_l = i
            res+=1
        elif i > i_r:
            i_r = i
            res+=1
    return res
        