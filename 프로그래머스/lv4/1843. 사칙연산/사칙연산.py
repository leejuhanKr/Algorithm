def solution(arr):
    memo = {}

    def foo(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if j - i == 1:
            memo[(i, j)] = [int(arr[i]),int(arr[i])]
            return memo[(i, j)]

        res = [-10e9, 10e9]
        for s in range(i + 1, j, 2):
            if arr[s] == "+":
                res[0] = max(res[0],foo(i, s)[0] + foo(s + 1, j)[0])
                res[1] = min(res[1],foo(i,s)[1] + foo(s + 1, j)[1])
            else:
                res[0] = max(res[0],foo(i, s)[0] - foo(s + 1, j)[1])
                res[1] = min(res[1],foo(i,s)[1] - foo(s + 1, j)[0])

        memo[(i, j)] = res
        return memo[(i, j)]

    return foo(0, len(arr))[0]