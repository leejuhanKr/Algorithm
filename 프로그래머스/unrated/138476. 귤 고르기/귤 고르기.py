from collections import Counter
def solution(k, tangerine):
    counter = Counter(tangerine)
    res = 0
    for _, amount in counter.most_common():
        k -= amount
        res += 1
        if k <=0: 
            break
    return res
    
    