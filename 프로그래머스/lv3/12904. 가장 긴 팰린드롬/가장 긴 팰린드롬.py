def solution(s):
    res = 1
    max_len = len(s)

    q = [
        *((i,i+1) for i in range(max_len-1)),
        *((i,i) for i in range(max_len)),
    ]

    while q:
        i,j = q.pop()
        if i>=0 and j<max_len and s[i] == s[j]:
            res = max(res, j-i+1)
            q.append((i-1,j+1))
        
    return res
        