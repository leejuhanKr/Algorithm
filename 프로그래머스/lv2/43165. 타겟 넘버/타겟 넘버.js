function solution(numbers, target) {
    let ans = 0
    const dfs = (idx, res) => {
        if (idx === numbers.length) {
            if (res === target) ans+=1
            return
        }
        // -= num
        dfs(idx+1, res-numbers[idx])
        // += num
        dfs(idx+1, res+numbers[idx])
    }
    dfs(0,0)
    return ans
}