def solution(n, money):
    dp = [1, *(0 for _ in range(n))]
    for m in money:
        for idx in range(m,n+1):
            dp[idx] = (dp[idx]+dp[idx-m])%1_000_000_007
    return dp[-1]
