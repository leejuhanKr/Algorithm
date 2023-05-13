def solution(arr, queries):
    maxsize = 10e9
    res = []
    for [s,e,k] in queries:
        v = maxsize
        for tmp in arr[s:e+1]:
            if k < tmp and v > tmp:
                v = tmp
        res.append(v if v != maxsize else -1)
    return res
        
        