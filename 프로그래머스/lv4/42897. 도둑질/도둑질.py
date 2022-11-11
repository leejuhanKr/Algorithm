def solution(money):
    if len(money) <= 2:
        return max(money, default=0)
    
    dp = [0, money[1], money[0], money[0]]

    for m in money[2:]:
        dp = [
            max(dp[0:2]),
            dp[0] + m,
            max(dp[2:4]),
            dp[2] + m,
        ]
    return max(dp[0:3])