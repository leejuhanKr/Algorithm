def solution(n, cores):
    processed = lambda arr,i: sum(i//c for c in arr)+len(cores)
    cond = lambda arr,i: processed(arr,i) < n
    
    t = bisect(cores, 0,max(cores)*n//len(cores), cond)
    n-=processed(cores,t)
    t+=1
    for i,c in enumerate(cores,1):
        if t%c == 0:
            n -= 1
            if not n:
                return(i)

def bisect(arr, l, r, cond):
    while l<=r:
        mid = (l+r)//2
        if cond(arr,mid): l = mid + 1
        else: r = mid - 1
    return r

            