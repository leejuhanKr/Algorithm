def solution(lottos, win_nums):
    a = 7-len(set(lottos).intersection(set(win_nums)))
    return [*map(lambda x: x if x!= 7 else 6 ,[a-lottos.count(0),a])]
    
    
