from itertools import combinations
from collections import Counter

def solution(orders, course):
    res = []
    orders = [set(o) for o in orders]
    
    for i in course:
        c_n = Counter() 
        for a,b in combinations(orders,2):
            for c in combinations(a&b,i):
                c_n += Counter([''.join(sorted(c))])

        if m_v := max(c_n.values(),default=0):
            res += [k for k,v in c_n.items() if v==m_v]
    
    return sorted(res)