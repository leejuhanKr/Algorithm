def solution(distance, scope, times):
    scope = map(sorted, scope)
    scope,times = zip(*sorted(zip(scope,times)))
    o = 0
    for t in range(1,distance+1):
        if scope[o][0] <= t <= scope[o][1]:
            if 1 <= t%sum(times[o]) <= times[o][0]:
                return t
            if t == scope[o][1]:
                o += 1
                if not (o < len(scope)):
                    return distance
    return distance
        