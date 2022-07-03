n = input()
a = map(int,input().split())
b = map(int,input().split())
diff = (i-j for i,j in zip(a,b))

ans = 0

hash = {}
ig = 0
for d in diff:
    ig += d
    hash.setdefault(ig,0)
    hash[ig] +=1

if 0 in hash:
    q=hash[0]
    ans += q
    if q >= 2:
        ans += ((q)*(q-1))//2
    del hash[0]

for q in hash.values():
    if q >= 2:
        ans += ((q)*(q-1))//2

print(ans)