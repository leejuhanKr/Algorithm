from queue import PriorityQueue

def solution(jobs):
    answer = 0
    jobs = sorted(jobs, reverse = True)
    num_of_jobs = len(jobs)
    task = PriorityQueue()
    time = 0
    total_time_lst=[]
    
    while len(total_time_lst) < num_of_jobs:
        # 해당 시간까지 들어온 요청 확인후 큐에 삽입
        print(f'현재 시간:{time}ms')
        while jobs and jobs[-1][0] <= time:
            job = jobs.pop()
            print(f'요청:{job}')
            task.put((job[1],job[0])) # (작업 시간, 요청 시간) -> 작업순위 우선시간
        
        if task.qsize():
            # 가장 빨리 처리 가능한 task 처리
            process =  task.get()

            print(f'처리:{process}')
            # 총 소요시간 계산
            wait_time = time - process[1]
            running_time = process[0]
            total_time = wait_time + running_time
            # 소요시간 리스트에 추가
            total_time_lst.append(total_time)

            time+=running_time
        else:
            time+=1

    answer = sum(total_time_lst)//len(total_time_lst)

    return answer