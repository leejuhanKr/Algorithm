def solution(n):
    n*=2
    res = [0]
    def back(i,_sum):
        if i == n:
            if _sum == 0:
                res[0]+=1
            return
        for v in (-1,1):
            k = _sum+v
            if 0 <= k < n-i:
                back(i+1,k)
                
    back(0,0)
    return res[0]

    
    