from collections import deque

def solution(players, m, k):
    res = 0;
    cur_servers = 0; # 증설 서버 개수
    
    q = deque() # (t: 종료 시간, n: 서버 개수)
    
    for t in range(0, 24):
        # 서버 종료
        while q and q[0][0] <= t:
            _, _n = q.popleft()
            cur_servers -= _n

        # 필요 증설 서버 개수
        needed = players[t] // m 
        
        
        # 서버 증설
        if needed > cur_servers:
            need_to_add = needed - cur_servers
            cur_servers += need_to_add
            q.append((t+k, need_to_add))
            res += need_to_add
            
    return res
    
    