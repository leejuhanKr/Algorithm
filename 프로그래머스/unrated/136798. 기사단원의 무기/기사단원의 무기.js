function solution(number, limit, power) {
    return Array
        .from({length: number}, (v, i) => i+1)
        .map(num => {
            cnt = -Number.isInteger(num**0.5)
            for (let d=1; d<=num**0.5; d++) {
                if (num%d == 0) cnt+=2
                if (cnt > limit) return power
            }
            return cnt
        })
        .reduce((acc,cur) => acc+cur)
}