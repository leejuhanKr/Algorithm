def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    both = lost.intersection(reserve)
    lost = lost.difference(both)
    reserve = reserve.difference(both)
    res = n-len(lost)
    for i in lost:
        for j in [i-1,i+1]:
            if j in reserve:
                res+=1
                reserve.remove(j)
                break
    return res