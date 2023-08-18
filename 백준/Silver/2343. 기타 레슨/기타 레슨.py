from sys import stdin


def bisect(arr, left, right, callback_cond):
    while left <= right:
        mid = (left + right) // 2
        if callback_cond(arr, mid):
            left = mid + 1
        else:
            right = mid - 1

    return right


def solution():
    N, M = map(int, stdin.readline().split())
    arr = [*map(int, stdin.readline().split())]

    def cond(arr, threshold):
        sum = 0
        cnt = 1
        for el in arr:
            sum += el
            if sum > threshold:
                cnt += 1
                sum = el

        return cnt > M

    res = bisect(arr, max(arr), sum(arr), cond) + 1

    return res


print(solution())
