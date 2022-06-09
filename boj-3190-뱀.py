# 뱀의 이동 규칙
# 먼저 몸길이를 늘려 머리를 다음칸에 위치
# 이동한 칸에 사과가 있다면, 사과 없어지고 꼬리는 움직이지 않음
# 이동한 칸에 사과가 있다면, 몸길이를 줄여 꼬리가 위치한 칸 비워줌

# 벽또는 자기 자신의 몸과 부딪히면 게임이 끝남

N = 6 # 보드의 크기 (2<=N<=100)
K = 3 # 사과의 개수 (0<=K<=100)
# 다음 K개의 줄 => 사과의 위치 / 행의 위치 열의 위치
apples = [
    (3, 4),
    (2, 5),
    (5, 3),
]
apples = set(apples)
L = 3 # 방향 변환 횟수 (1<=L<=100)
# 다음 L개의 줄 => 방향 변환 정보/ x:int c:char
# x: 게임 시작 시간으로부터 x초가 끝난 뒤에
# c:{L:left, D:rigth} 방향으로 회전
directions = [
    [3, 'D'],
    [15, 'L'],
    [17, 'D'],
]
# if __name__ = "__main__"

# N = int(input())
# K = int(input())
# apples = {tuple(map(int,input().split())) for _ in range(K)}
# print(f'{apples=}')
# L = int(input())
# directions = [input().split()for _ in range(L)]
# for i,v in enumerate(directions):
#     directions[i][0] = int(v[0])
# print(f'{directions=}')
from collections import deque
time = snake = deque([(1,1)])
seq = 0
dir = (0,1)
over_dir_flag = False

def change(dir,tran):
    # 0,1 => -1,0 / 1,0
    # 0,-1 => 1,0/ -1,0
    # 1,0 => 0,1/ 0,-1  
    # -1,0 => 0,-1 / 0,1
    x,y = dir
    tran = {'L': -1, 'D': 1}[tran]
 
    if x == 0:
        return (y*tran, 0)
    else:
        return (0, -x*tran)

cnt = 3
while cnt:
    head = snake[0]
    time += 1
    head = (head[0]+dir[0], head[1]+dir[1])

    # 대가리 삐져나오거나 부딪치는지 확인 
    if not all((
        head not in snake,
        1 <= head[0] <= N,
        1 <= head[1] <= N,
    )):
        break

    snake.appendleft(head)
    if head in apples:
        apples.remove(head)
    else:
        snake.pop()

    if (not over_dir_flag) and time == directions[seq][0]:
        dir = change(dir,directions[seq][1])
        seq += 1
        if seq == len(directions):
            over_dir_flag = True

print(time)





