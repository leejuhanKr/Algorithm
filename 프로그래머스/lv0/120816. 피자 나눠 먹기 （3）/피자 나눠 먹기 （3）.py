def solution(slice, n):
    r,q = divmod(n,slice)
    return r+ (q!=0)