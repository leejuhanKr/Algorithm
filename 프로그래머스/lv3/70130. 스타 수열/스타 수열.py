from collections import Counter

def solution(a):
    counter = Counter(a)
    prev = {k:[k, True] for k in counter}

    res = 0    
    for k in counter:
        if counter[k] > res or 1:
            cnt = 0
            for v in a:
                if prev[1][k]:
                    prev[k] = [v, False]
                elif (k == prev[k][0]) ^ (v==k):
                    cnt+=1
                    prev[k][1] = True
            res = max(res, cnt)

    return res*2
