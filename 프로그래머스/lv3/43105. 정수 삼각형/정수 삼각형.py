def solution(triangle):
    dp = triangle[0]
    for row in triangle[1:]:
        dp = [
            row[0]+dp[0],
            *(v+max(dp[i-1], dp[i]) for i, v in enumerate(row[1:-1],1)),
            row[-1]+dp[-1],
        ]
    return max(dp)