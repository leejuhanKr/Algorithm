def solution(n, times):
    cond = lambda times, time: sum(time//el for el in times) >= n
    
    def bisect(arr,l,r,cond):
        while l<=r:
            mid = (l+r)//2
            if cond(arr, mid):
                r = mid - 1
            else:
                l = mid + 1
        return l

    return bisect(times, 0, n*(max(times)//len(times)+1), cond)