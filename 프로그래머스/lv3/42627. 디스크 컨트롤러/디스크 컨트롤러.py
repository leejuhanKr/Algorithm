import heapq as hq

def solution(jobs):
    res = []
    time = 0

    jobs.sort()
    job_idx = 0
    job_length = len(jobs)
    
    will_pending = 0
    q = [] #heapq
    
    while True:
        # q에 job 추가
        while job_idx<job_length and jobs[job_idx][0] <= time:
            request_time, cost = jobs[job_idx]
            hq.heappush(q, [cost, request_time])
            job_idx += 1
        # 처리중인 일이 없다면 작업 시작
        if will_pending <= time and q:
            cost, request_time = hq.heappop(q)
            res.append(time-request_time+cost)
            will_pending = time + cost
            time = will_pending
        else:
            time += 1
        
        if job_idx==job_length and not q:
            return sum(res)//len(res)
            
    

        
        
        
        
        
    
    
    
    
