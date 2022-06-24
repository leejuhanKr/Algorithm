function solution(n) {
    let [a,b] = [0,1]
    let i = 0
    while (i < n) {
        [a,b] = [b, a+b].map(v=>v%1000000007)
        i++
    }
    return b
}