from collections import Counter

def solution(want, number, discount):
    cnt = Counter(dict(zip(want,number)))
    cnt.subtract(Counter(i for i in discount[:10] if i in cnt))
    res = +all(map(lambda x: x <= 0, cnt.values()))
    for m,n in zip(discount, discount[10:]):
        if m in cnt:
            cnt[m] +=1
        if n in cnt:
            cnt[n] -=1
        res += all(map(lambda x: x <= 0, cnt.values()))
    return res
    
    