# def solution(triangle):
#     dp = triangle[0]
#     for row in triangle[1:]:
#         dp = [
#             row[0]+dp[0],
#             *(v+max(dp[i-1], dp[i]) for i, v in enumerate(row[1:-1],1)),
#             row[-1]+dp[-1],
#         ]
#     return max(dp)
from functools import lru_cache


def solution(triangle):
    max_step = len(triangle) - 1

    @lru_cache(maxsize=250000)
    def clac(idx, step):
        if step == max_step:
            return triangle[max_step][idx]
        return triangle[step][idx] + max(clac(idx, step + 1), clac(idx + 1, step + 1))

    return clac(0, 0)
    