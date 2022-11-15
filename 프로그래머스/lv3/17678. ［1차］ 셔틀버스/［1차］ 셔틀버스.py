def solution(n, t, M, timetable):
    res = "00:00"
    timetable.sort()
    wait = 0
    t_i = 0
    bus = '09:00'
    n_i = 0
    for h in range(24):
        for m in range(60):   
            if n_i==n:
                return res
            
            time = f'{h:0>2}:{m:0>2}'
            
            while t_i<len(timetable) and timetable[t_i] <= time:
                wait+=1
                t_i+=1
                flag =1
                
            if wait < M*(n-n_i):
                res = time
                
            if bus == time:
                print(f'bus == {time}',wait -M)
                wait -= M
                if wait < 0:
                    res = time
                    wait = 0
                
            if bus <= time:
                n_i += 1
                _h,_m = divmod(t*n_i,60)
                bus = f'{9+_h:0>2}:{_m:0>2}'

                

                    
                
    
