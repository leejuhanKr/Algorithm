# 격자의 크기를 뜻하는 정수 n, m,
# 출발 위치를 뜻하는 정수 x, y,
# 탈출 지점을 뜻하는 정수 r, c,
# 탈출까지 이동해야 하는 거리를 뜻하는 정수 k가 매개변수로 주어집니다.
# 이때, 미로를 탈출하기 위한 경로를 return 하도록 solution 함수를 완성해주세요.
# 단, 위 조건대로 미로를 탈출할 수 없는 경우 "impossible"을 return 해야 합니다.

# l: 왼쪽으로 한 칸 이동
# r: 오른쪽으로 한 칸 이동
# u: 위쪽으로 한 칸 이동
# d: 아래쪽으로 한 칸 이동
# d > l > r > u
# ⬇️  ⬅️   ➡️  ⬆️

# 제한사항
# 2 ≤ n (= 미로의 세로 길이) ≤ 50
# 2 ≤ m (= 미로의 가로 길이) ≤ 50
# 1 ≤ x ≤ n
# 1 ≤ y ≤ m
# 1 ≤ r ≤ n
# 1 ≤ c ≤ m
# (x, y) ≠ (r, c)
# 1 ≤ k ≤ 2,500
# 입출력 예
# n	m	x	y	r	c	k	result
# 3	4	2	3	3	1	5	"dllrl"
# 2	2	1	1	2	2	2	"dr"
# 3	3	1	2	3	3	4	"impossible"


FAIL = "impossible"


def solution(n: int, m: int, x_i: int, y_i: int, x_f: int, y_f: int, k):

    path = [''] * k

    PRIORITY_COMMEND = [
        [(1,0),'d'],
        [(0,-1),'l'],
        [(0,1),'r'],
        [(-1,0),'u'],
    ]

    # status=> 0: pending, 1:success
    status = [0]
    res = [FAIL]
    def back(x:int ,y:int ,path_idx:int):
        print(x,y, path_idx, status[0])
        if not (1 <= x <= n) or not (1 <= y <= m) or status[0] != 0:
            return
        
        if path_idx >= k:
            if path_idx == k and (x == x_f and y == y_f):
                res[0] = path.copy()
                status[0] = 1
            return

        for (dx,dy), command in PRIORITY_COMMEND:
            path[path_idx] = command
            back(x+dx, y+dy, path_idx+1)
    
    back(x_i, y_i, 0)

    if status[0] == 0:
        return FAIL
    return ''.join(res[0])

    # while stack:
    #     (x, y), path = stack.pop()

    #     if not (1 <= x <= n) or not (1 <= y <= m):
    #         continue

    #     if path_idx >= k:
    #         if path_idx == k and (x == x_f and y == y_f):
    #             return path
    #         continue

    #     for (dx, dy), next_command in priority_commend:
    #         path[path_idx] = next
    #         next_node = ((x+dx, y+dy), path_idx+1)
    #         stack.append(next_node)

    # return FAIL

실행한 결괏값 "uuuuu"이 기댓값 "dllrl"과 다릅니다.
출력 〉	
2 3 0 0 ['', '', '', '', '']
3 3 1 0 ['d', '', '', '', '']
4 3 2 0 ['d', 'd', '', '', '']
3 2 2 0 ['d', 'l', '', '', '']
4 2 3 0 ['d', 'l', 'd', '', '']
3 1 3 0 ['d', 'l', 'l', '', '']
4 1 4 0 ['d', 'l', 'l', 'd', '']
3 0 4 0 ['d', 'l', 'l', 'l', '']
3 2 4 0 ['d', 'l', 'l', 'r', '']
4 2 5 0 ['d', 'l', 'l', 'r', 'd']
3 1 5 0 ['d', 'l', 'l', 'r', 'l']
3 3 5 1 ['d', 'l', 'l', 'r', 'r']
2 2 5 1 ['d', 'l', 'l', 'r', 'u']
2 1 4 1 ['d', 'l', 'l', 'u', 'u']
3 3 3 1 ['d', 'l', 'r', 'u', 'u']
2 2 3 1 ['d', 'l', 'u', 'u', 'u']
3 4 2 1 ['d', 'r', 'u', 'u', 'u']
2 3 2 1 ['d', 'u', 'u', 'u', 'u']
2 2 1 1 ['l', 'u', 'u', 'u', 'u']
2 4 1 1 ['r', 'u', 'u', 'u', 'u']
1 3 1 1 ['u', 'u', 'u', 'u', 'u']

"dllrl"