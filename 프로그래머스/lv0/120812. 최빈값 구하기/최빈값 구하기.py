from collections import Counter

def solution(array):
    res = Counter(array).most_common(2)
    return -1 if len(res) == 2 and res[0][1] == res[1][1] else res[0][0]