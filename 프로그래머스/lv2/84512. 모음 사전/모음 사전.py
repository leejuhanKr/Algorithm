def solution(word):
    _dict = {'A':1, 'E':2, 'I':3, 'O':4, 'U':5}
    word = [_dict[w] for w in word]
    n=5
    a= [5**i for i in range(5)]
    for i in range(1,5):
        a[i]+=a[i-1]

    ans = 0
    for i in word:
        ans += a[n-1]*(i-1)+1
        n-=1
        
    return ans