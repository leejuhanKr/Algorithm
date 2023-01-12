from collections import Counter
def solution(N, stages):
    arrival = len(stages)
    ans = {i:0 for i in range(1,N+1)}
    on_stage = Counter(stages)
    for i in range(1,N+1):
        if on_stage[i]:
            ans[i] = on_stage[i]/arrival
            arrival -= on_stage[i]
    ans = sorted(ans.items(), key=lambda x: (x[1],-x[0]), reverse=True)
    return [i for i,j in ans]