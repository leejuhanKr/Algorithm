from sys import maxsize

def solution(sequence, k):
    s, e = 0, -1
    _len = maxsize
    sum = 0
    res = [s, e]
    for idx, num in enumerate(sequence):
        e=idx
        sum += num
        while sum > k:
            sum -= sequence[s]
            s+=1
        if sum == k:
            if _len > e - s:
                _len = e-s
                res = (s,e)
            sum -= sequence[s]
            s+=1
    return res
            
            

