def solution(arr, k):
    res = []
    for v in arr:
        if len(res) >= k:
            return res
        if v not in res:
            res.append(v)
    else:
        return res + [-1] * (k-len(res))