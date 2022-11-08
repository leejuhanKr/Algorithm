def solution(n, info):
    info.reverse()
    stack = []
    target = [0]*11
    max_score = 0
    res = target.copy()
    
    stack.append((1,target,0,n))
    while stack:
        tmp, tmp_target, tmp_score, rest = stack.pop()
        if tmp > 10:
            if tmp_score < max_score:
                continue
            tmp_target[0] = rest
            if tmp_score > max_score:
                max_score = tmp_score
                res = tmp_target     
                continue
            if tmp_score == max_score and max_score!=0:
                res = max(res, tmp_target)
                continue
            continue
        
        required = info[tmp] + 1
        if required <= rest:
            next_target = tmp_target.copy()
            next_target[tmp] = required
            stack.append((tmp+1, next_target, tmp_score+tmp, rest-required))
        stack.append(
            (tmp+1, tmp_target.copy(), tmp_score-(tmp if info[tmp] else 0), rest)
        )
        
    return list(reversed(res)) if any(res) else [-1]
        
    