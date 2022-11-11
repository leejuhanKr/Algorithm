def solution(n, stations, w):
    empty_space = []
    a = 1
    for p in stations:
        if (dist:= (p-w)-a) > 0:
            empty_space.append(dist)
            a = p+w+1
        else:
            a = p+w+1
    if (dist:= n-a) >= 0:
        empty_space.append(dist+1)
    
    coverage = w*2+1
    
    def check(arr, m): # arr = empty_space
        for d in arr:
            q,r = divmod(d, coverage)
            m -= q+1 if r else q
            if m < 0:
                return False
        return True
    
    return bisect(empty_space, 0, n//coverage, check)

    
def bisect(arr,l,r,cond): # 조건을 만족하는 값중 가장 왼쪽에 있는 값
    while l <= r:
        mid = (l+r)//2
        if cond(arr,mid):
            r = mid-1
        else:
            l = mid+1
    return l