from sys import stdin
N,C = map(int,input().split())
X = list(map(int,stdin.readlines()))

X.sort()
d = [X[i]-X[i-1] for i in range(1,len(X))]
# print(d)
def check(d,c,t):
    sum=0
    i=0
    c-=1
    for i in d:
        sum+=i
        if sum >= t:
            c-=1
            sum=0
        if not c:
            return True
    return False

# check(d,C,3)

l,r=0, X[-1]-X[0]
while l<=r:
    m = (l+r)//2
    # print(l,m,r)
    if check(d,C,m):
        l=m+1
    else:
        r=m-1
    # print(l,m,r)

print(r)