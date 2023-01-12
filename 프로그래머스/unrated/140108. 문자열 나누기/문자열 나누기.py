def solution(s):
    res = 0
    cnt = 0
    base = None
    for c in s:
        if not base:
            base = c
            cnt = 1
            res += 1
        else:
            if c == base:
                cnt += 1
            else:
                cnt -= 1
            
            if cnt == 0:
                base = None
                
    return res
            
        