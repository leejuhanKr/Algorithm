from collections import deque
from sys import stdin
n_max = int(input())
start, end = map(lambda x: int(x)-1, input().split())
n_line = int(input())
lines = [tuple(map(int,stdin.readline().split())) 
    for _ in range(n_line)]

map_ = [[0]*n_max for _ in range(n_max)]
for line in lines:
    r,c = line[0]-1, line[1]-1
    map_[r][c] = -1
    map_[c][r] = -1

visited=deque()
visited.append(start)
map_[start][start]=0

def bfs():
    while visited:
        tmp = visited.popleft()
        tmp_ans = map_[tmp][tmp]
        if tmp == end:
            return tmp_ans

        for i,v in enumerate(map_[tmp]):
            if v == -1:
                visited.append(i)
                map_[tmp][i] = 0
                map_[i][tmp] = 0
                map_[i][i] = tmp_ans+1
    return -1

print(bfs())