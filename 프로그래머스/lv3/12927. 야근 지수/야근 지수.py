# import heapq as hq

# def solution(n, works):
#     clac_work = lambda arr,t: sum(rest for w in works if (rest:=w-t) > 0) 
#     cond = lambda arr,t: clac_work(arr,t) <= n

#     t = bisect(works, 0, 50_000, cond)
#     rest = n-clac_work(works,t)
    
#     q = []
#     for i in range(len(works)):
#         hq.heappush(q,-min(t,works[i]))
        
#     res = 0
#     while q:
#         el = -hq.heappop(q)
#         if rest and el > 0:
#             rest -= 1
#             el -= 1
#         res += el**2
#     return res

# def bisect(arr,l,r,cond):
#     while l<=r:
#         mid = (l+r)//2
#         if cond(arr, mid):
#             r = mid-1
#         else:
#             l = mid+1
#     return l

import heapq as hq

def solution(n, works):
    res = 0
    
    q = [-i for i in works]
    hq.heapify(q)
    while n and q[0] < 0:
        el = hq.heappop(q)
        hq.heappush(q,el+1)
        n-=1
    return sum(i**2 for i in q)
        
        
    