n = int(input())
arr = input().split()
def func(a, l, b):
    ans = [-1] * (n + 1)
    i, j = 0, 0
    while j < n:
        if arr[j] == a:
            for k in range(j, i - 1, -1):
                ans[k] = l
                l += b
            i = j + 1
        j += 1
    for k in range(j, i - 1, -1):
        ans[k] = l
        l += b
    print(''.join(map(str, ans)))
    return
func('>', 9, -1)
func('<', 0, 1)