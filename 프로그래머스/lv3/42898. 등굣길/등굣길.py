# from collections import defaultdict
def solution(m, n, puddles):
    _map = {(1,1):1 , **{(i,j): 0 for i,j in puddles}}

    def helper(i,j):
        if (v:=_map.get((i,j))) != None:
            return v
        if i==0 or j ==0:
            return 0
        _map[(i,j)] =  (helper(i-1,j)+helper(i,j-1))%1_000_000_007
        return _map[(i,j)]

    return helper(m,n)