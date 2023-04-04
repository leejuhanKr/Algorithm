# 파라메트릭 이분탐색에 관한 고찰 ㅎㅎ(백준 2110)
n, c = 5, 3
arr = [1, 2, 8, 4, 9]
arr.sort()  # [1, 2, 4, 8, 9]


def cond(arr, c):
    """
    c개의 공유기를 설치했을때
    공유기 사이의 거리의 최소값의 최댓값이 mid보다 같거나 클수 있는지 여부 반환
    """

    def helper(target):
        # 최댓값을 만족하면서 공유기를 설치했을때 공유기가 남으면 최댓값이 아닌 것
        # 최댓값을 더 줄일 수 있다 => False
        prev_pos = arr[0]
        # 양쪽끝 공유기 설치
        cnt = c - 2
        tmp_dist = 0
        for tmp_pos in arr[1:-1]:
            tmp_dist += tmp_pos - prev_pos
            if tmp_dist >= target:
                cnt -= 1
                if cnt < 0:
                    return True
                tmp_dist = 0
            prev_pos = tmp_pos
        tmp_pos = arr[-1]
        tmp_dist += tmp_pos - prev_pos
        if cnt == 0 and tmp_dist >= target:
            return True
        return False

    return helper


cb = cond(arr, c)
print(cb(2.9))
print(cb(3))
print(cb(3.1))
print(cb(4))
# print(cb(3.2))

# print(cb(2.9, arr, c)) #t
# print(cb(3, arr, c))    #t
# print(cb(3.1, arr, c))  #f


def bisect(l, r, cb):
    while l <= r:
        mid = (l + r) // 2
        if cb(mid):
            l = mid + 1
        else:
            r = mid - 1
    return r


# def cond(arr, target):
#     def helper(mid_idx):
#         return arr[mid_idx] <= target
#     return helper

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# cb = cond(arr,3)


print(bisect(0, arr[-1] - arr[0], cb))

from functools import reduce

solution = lambda m: max(
    reduce(
        lambda a, c: [max(a[:2]), a[0] + c, max(a[2:]), a[2] + c],
        m[2:],
        [0, m[1], m[0], m[0]],
    )
)
