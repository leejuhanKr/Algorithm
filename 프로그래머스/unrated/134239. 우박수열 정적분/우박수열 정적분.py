def solution(k, ranges):
    ks = []
    while k != 1:
        nk = k//2 if k%2==0 else k*3 + 1
        ks.append(sum((k,nk))/2)
        k=nk
    return [
        sum(ks[i:len(ks)+j]) if i<=len(ks)+j else -1
        for i,j in ranges
    ] 
