from collections import namedtuple

distance = 10
scope = [[3,4],[5,8]]
times = [[2,5],[4,3]]
result = 8

# def solution(distance, scope, times):
#     t = 0
#     p = 0
    
#     while true:
#         go_without_hazzard()
#         if not is_passed:
#             break
#         go_hazzard()
#         if not is_passed:
#             break
        
#     return t

Work = namedtuple('Work',('scope','times'))
Scope = namedtuple('Scope',('start','end'))
works = [Work(Scope(*s),t) for s, t in zip(scope,times)]
works.sort(key=lambda x: x.scope[0])
p = 0
dp = 0



for scope, times in works:
    _p = scope.start-1
    for _p in range(scope.start, scope.end+1):
        print(f'{_p=}')
        if (times[0]-(_p%sum(times)))>=0:
            print((times[0]-(_p%sum(times))))
            print(_p)
        