n,k = map(int,input().split())
A = [int(i) for i in input().split()]
P = [int(i) for i in input().split()]


inf = float('inf')
visited = [0]*n
ans = [0]

def dfs(visited,k,acc,res):
    ans[0] = max(res,ans[0])
    for i,is_visited in enumerate(visited):
        if is_visited:
            continue
        if k-acc-A[i] >= 0:
            visited[i]=1
            dfs(visited,k-acc-A[i],acc+A[i],res+P[i])
            visited[i]=0

dfs(visited,k,0,0)

print(ans[0])