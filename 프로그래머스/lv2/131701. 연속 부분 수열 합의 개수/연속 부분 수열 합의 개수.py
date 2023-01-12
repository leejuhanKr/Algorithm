def solution(els):
    res = set(els)
    sums = els
    for i in range(1,len(els)):
        sums = [sum(ns) for ns in zip(sums,els[i:]+els[:i])]
        res |= set(sums)
    return len(res)
        
        

    