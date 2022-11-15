def solution(N, T, M, timetable):
    res, bus = "00:00", "09:00"
    timetable.sort()
    wait, t_i, n_i = 0, 0, 0
    for h in range(24):
        for m in range(60):   
            if n_i==N:
                return res
            
            time = f'{h:0>2}:{m:0>2}'
            
            while t_i<len(timetable) and timetable[t_i] <= time:
                wait+=1
                t_i+=1
                
            if wait < M*(N-n_i):
                res = time
                
            if bus == time:
                wait -= M
                if wait < 0:
                    res = time
                    wait = 0
                
            if bus <= time:
                n_i += 1
                _h,_m = divmod(T*n_i,60)
                bus = f'{9+_h:0>2}:{_m:0>2}'
