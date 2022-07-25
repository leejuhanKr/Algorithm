e,s,m = map(int,input().split())

def g(v):
    while True:
        yield from range(1,v+1)

for res, (E,S,M) in enumerate(zip(g(15), g(28), g(19)),1):
    if all((e==E, s==S, m==M)):
        print(res)
        break
    res+=1