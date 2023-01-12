def solution(sticker):
    _len = len(sticker)
    dp = [[0,0,0,0] for _ in range(_len)]
    # dp[i][0] : dp[0] 뜯고 i 안뜯었을때 최댓값
    # dp[i][1] : dp[0] 뜯고 i 뜯었을때 최댓값
    # dp[i][2] : dp[0] 안뜯고 i 안뜯었을때 최댓값
    # dp[i][3] : dp[0] 안뜯고 i 뜯었을때 최댔값
    if _len == 1:
        return sticker[0]

    dp[1] = [sticker[0], sticker[0], 0, sticker[1]]
    
    for i in range(2,_len):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1])
        dp[i][1] = dp[i-1][0]+sticker[i]
        dp[i][2] = max(dp[i-1][2], dp[i-1][3])
        dp[i][3] = dp[i-1][2]+sticker[i]
    
    return max(dp[-1][0],dp[-1][2],dp[-1][3])
        