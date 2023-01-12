from collections import defaultdict
from typing import Counter

def solution(X, Y):
    x, y = freq(X), freq(Y)
    res = ''
    for n in "987654321":
        res += n*min(x[n],y[n])
    if res != '':
        return res+'0'*min(x['0'],y['0'])
    if x['0'] and y['0']:
        return '0'
    return '-1'

def freq(word:str):
    _dict = defaultdict(int)
    _dict.update(Counter(list(word)))
    return _dict
