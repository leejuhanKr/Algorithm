from sys import stdin
input = stdin.readline

from collections import deque

# n_com = 7
# n_link = 6
# links =[
#     (1, 2),
#     (2, 3),
#     (1, 5),
#     (5, 2),
#     (5, 6),
#     (4, 7),]
n_com = int(input())
n_link = int(input())

arr = [[None]*n_com for _ in range(n_com)]

for _ in range(n_link):
    a, b = map(int,input().split())
    a, b = a-1, b-1
    arr[a][b] = True
    arr[b][a] = True

ans=set([0])
queue = deque([0])
while queue:
    i = queue.popleft()
    # ans.add(i)
    tmp=[]
    for j,v in enumerate(arr[i]):
        if (v==True) and (j not in ans):
            queue.append(j)
            ans.add(j)
    # print(queue)

print(len(ans)-1)