def solution(m):
    if len(m) <= 2:
        return max(m, default=0)
    dp = [0, m[1], m[0], m[0]]
    for c in m[2:]:
        dp = [max(dp[:2]), dp[0] + c, max(dp[2:]), dp[2] + c]
    return max(dp[:3])

# def solution(money):
#     if len(money) <= 2:
#         return max(money, default=0)
    
#     dp = [0, money[1], money[0], money[0]]

#     for m in money[2:]:
#         dp = [
#             max(dp[0:2]),
#             dp[0] + m,
#             max(dp[2:4]),
#             dp[2] + m,
#         ]
#     return max(dp[0:3])