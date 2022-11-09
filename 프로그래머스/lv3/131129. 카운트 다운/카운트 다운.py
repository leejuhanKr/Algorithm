from collections import deque
def solution(target):
    dp = [[] for _ in range(target+1)] # idx: 점수, el: (다트수, 싱글 + 불)
    dp[0].append((0,0))

    for score in range(target+1):
        dp[score] = sorted(dp[score], key=lambda x: (x[0],-x[1]))[0]
        dart, bonus = dp[score] 
        for v in range(1,21):
            if score+v <= target:
                dp[score+v].append((dart+1, bonus+1))
            for w in range(2,4):
                if score+v*w <= target:
                    dp[score+v*w].append((dart+1, bonus))
        if score+50 <= target:
            dp[score+50].append((dart+1, bonus+1))

    return dp[-1]
    