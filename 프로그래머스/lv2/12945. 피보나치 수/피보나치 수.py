def solution(n):
    memo = [0,1]
    for i in range(2,n+1):
        memo.append(sum(memo[i-2:i])%1234567)
        
    return memo[n]