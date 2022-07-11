# %%
from collections import deque
from sys import stdin
input = stdin.readline
N,K = map(int, input().split())
I = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

#%% virus_map 초기화
sec=0
virus_map = [[] for _ in range(K+1)]
for i in range(N):
    for j in range(N):
        if virus:=I[i][j]:
            virus_map[virus].append((sec,i,j))
            
#%% queue초기화
origin=[]
for virus in range(1,K+1):
    origin+=(virus_map[virus])

queue = deque(origin)

#%% bfs
direction = (
            (-1, 0),
            (1, 0),
            (0, 1),
            (0, -1)
            )

while queue:
    sec,x,y = queue.popleft()
    if sec==S:
        break
    virus = I[x][y]
    for d_x, d_y in direction:
        n_x, n_y = x+d_x, y+d_y
        if (0<=n_x<N) and (0<=n_y<N) and (I[n_x][n_y]==0):
            I[n_x][n_y] = virus
            queue.append((sec+1,n_x,n_y))

print(I[X-1][Y-1])