def solution(n, k):
    tri = ""
    while True:
        n,r = divmod(n,k)
        tri += str(r)
        if not n:
            break
    tri = '0' + tri[::-1] + '0'
    
    candidate = [int(i) for i in tri.split('0') if i]
    
    ans=0
    for num in candidate:
        if num==1:
            continue
        for i in range(2,int(num**0.5)+1):
            if not num%i:
                break
        else:
            ans+=1

    return ans