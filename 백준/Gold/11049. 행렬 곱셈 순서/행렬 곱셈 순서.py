import sys

input = sys.stdin.readline

n = int(input())
mat_info = [*map(int, input().split())]
for _ in range(n - 1):
    mat_info.append(int(input().split()[1]))


def solution(n, mat):
    arr = [[-1] * (n) for _ in range(n)]
    for s in range(n):
        e = s
        arr[s][e] = 0

    for d in range(1, n):
        for s, e in zip(range(n - d), range(d, n)):
            res = sys.maxsize
            S = mat[s]
            E = mat[e + 1]

            for m in range(s + 1, e + 1):
                _res = S * mat[m] * E + arr[s][m - 1] + arr[m][e]
                res = min(res, _res)
            arr[s][e] = res

    return arr


ans = solution(n, mat_info)
print(ans[0][-1])