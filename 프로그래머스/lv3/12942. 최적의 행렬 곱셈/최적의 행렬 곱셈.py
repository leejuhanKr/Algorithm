def solution(mats):
    mats_len = len(mats)
    dp = [[0]*(mats_len) for _ in range(mats_len)]
    for d in range(1,mats_len):
        for i,k in zip(range(mats_len-d),range(d,mats_len)):
            dp[i][k] = min(
                dp[i][j]+dp[j+1][k]+mats[i][0]*mats[j][1]*mats[k][1]
                for j in range(i,k)
            )

    return dp[0][mats_len-1]
    
            