import sys
from collections import deque
from collections import defaultdict
input=sys.stdin.readline
N,n,root=map(int,input().split())
lst={}
lst=defaultdict(set)

for i in range(n):
    x,y=map(int,input().split())
    lst[x].update([y])
    lst[y].update([x])
    
def dfs(graph,root):
    visited=[];stack=[root]
    while stack:
        k=stack.pop()
        if k not in visited:
            visited.append(k)
            stack.extend(sorted(graph[k]-set(visited),reverse=True))
    return visited

visited = [str(i) for i in dfs(lst,root)]
print(" ".join(visited))

def bfs(graph,root):
    visited=[]; que= deque([root])
    while que:
        k=que.popleft()
        if k not in visited:
            visited.append(k)
            que +=(sorted(graph[k]-set(visited)))
    return visited

visited = [str(i) for i in bfs(lst,root)]
print(" ".join(visited))