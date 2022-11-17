function solution(numbers) {
    const ws = Array.from(Array(10), () => Array(10).fill(1))
    for (let i = 0; i < 10; i++) {
        for (let j = 0; j<i; j++) {
            ws[j][i] = ws[i][j] = getWeigth(i,j)
        }
    }

    p = 4
    dp = [[6,0]]
    next = new Map()
    for (n of numbers) {
        next.clear()
        n = +n
        for (let [pp, v] of dp) {
            for (let [remain, replace] of [[p,pp], [pp,p]])
            if (remain !== n) {
                a = Math.min(next.get(remain)||Infinity, v+ws[replace][n])
                next.set(remain,a)
            }
        }
        dp = Array.from(next)
        p=n
    }
    return Array.from(next.values()).reduce((acc,cur) => Math.min(acc, cur), Infinity)
}

const getPos = (n) => [Math.floor((n-1)/3), (n-1)%3]

const getWeigth = (n1,n2) => {
    if (n1 === n2) return 1

    let  [[x1,y1],[x2,y2]] = [n1,n2].map(v => v===0?11:v).map(getPos)
    const [dx,dy] = [x1-x2,y1-y2].map(Math.abs)
    return Math.max(dx,dy)+dx+dy
}