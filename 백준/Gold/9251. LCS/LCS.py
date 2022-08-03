import sys
sys.setrecursionlimit(10000)


def lcs(str1, str2):
    memo = [[-1 for _ in str2+'_'] for _ in str1+'_']

    def f(l, r):
        if l >= len(str1) or r >= len(str2):
            return 0
        if memo[l][r] != -1:
            return memo[l][r]

        if str1[l] == str2[r]:
            memo[l][r] = 1 + f(l+1, r+1)
            return memo[l][r]

        memo[l+1][r] = f(l+1, r)
        memo[l][r+1] = f(l, r+1)

        return max(memo[l+1][r], memo[l][r+1])
    return f(0, 0)


str1 = input()
str2 = input()
print(lcs(str1, str2))