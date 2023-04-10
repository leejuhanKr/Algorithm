from sys import maxsize

def solution(seq, k):
    head = enumerate(seq,1)
    _sum = 0
    si, se, rsi, rei = 0, 0, 0, maxsize
    for ei, ev in enumerate(seq):
        _sum += ev
        while _sum > k:
            si, sv = next(head)
            _sum -= sv
        if _sum == k and ei-si < rei-rsi:
            rsi, rei = si, ei
    return [rsi, rei]

