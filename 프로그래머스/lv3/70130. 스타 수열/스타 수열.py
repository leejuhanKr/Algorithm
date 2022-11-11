from collections import Counter

def solution(a):
    counter = Counter(a)
    prev = dict.fromkeys(counter, False)
    res = 0    
    for i in prev:
        if counter[i] > res:
            cnt = 0
            for v in a:
                if type(prev[i]) is bool:
                    prev[i]=v
                elif (i == prev[i]) ^ (v==i):
                    cnt+=1
                    prev[i]= False
            res = max(res, cnt)
    
    return res*2
