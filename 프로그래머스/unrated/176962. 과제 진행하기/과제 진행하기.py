from operator import itemgetter

def timestamp(_str):
    h, m = map(int, _str.split(':'))
    return h*60 + m

def preprocess_plan(plan):
    subject, start_time, required_time = plan
    return subject, timestamp(start_time), int(required_time)

def solution(plans):
    complete = []
    pending = []
    plans = [*map(preprocess_plan, plans)]
    plans.sort(key=itemgetter(1))
    
    for idx, plan in enumerate(plans):
        subject, start_time, required_time = plan

        next_time = plans[idx+1][1] if idx+1 < len(plans) else 10e9
        left_time = next_time - (start_time + required_time)
        if left_time > 0:
            complete.append(subject)
            while left_time and pending:
                subject, required_time = pending.pop()
                left_time -= required_time
                if left_time >= 0:
                    complete.append(subject)
                    if left_time == 0:
                        break
                else:
                    pending.append([subject, -left_time])
                    break
                
        elif left_time < 0:
            pending.append([subject, -left_time])
        else:
            complete.append(subject)
        
    return complete