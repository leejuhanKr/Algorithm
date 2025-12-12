from collections import deque

def solution(players, m, k):
    res = 0
    q = deque()  # (만료 시간, 서버 수)
    cur_servers = 0  # 현재 운영 중인 증설 서버 수
    
    for t in range(24):
        # 1. 만료된 서버 반납
        while q and q[0][0] <= t:
            _, expired = q.popleft()
            cur_servers -= expired
        
        # 2. 필요한 서버 수 계산
        needed = players[t] // m  # n x m 이상이면 n대 필요
        
        # 3. 증설 필요 여부 확인
        if needed > cur_servers:
            add = needed - cur_servers
            cur_servers += add
            q.append((t + k, add))  # k시간 후 만료
            res += add
    
    return res