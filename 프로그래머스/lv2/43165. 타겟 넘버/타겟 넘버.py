def solution(numbers, target):
    answer = dfs(numbers,target,0)
    return answer

def dfs(numbers, target, ans):

    if not numbers:
        return ans + (target == 0)
    
    ans = ans\
        +dfs(numbers[1:], target+numbers[0],ans)\
        +dfs(numbers[1:], target-numbers[0],ans)
    
    return ans