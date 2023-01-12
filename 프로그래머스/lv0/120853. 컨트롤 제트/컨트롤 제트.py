def solution(s):
    res = []
    for i in s.split():
        if res and i=='Z':
            res.pop()
        else:
            res.append(int(i))
    return sum(res)
        
        