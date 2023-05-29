function solution(arr) {
    let i = 0
    let flag
    while (flag = true) {
        arr = arr.map((v) => {
            const newV = (v%2==0 && v>50) ? v/2 : (v%2==1 && v < 50) ? v*2 + 1 : v
            if (flag && v!=newV) {
                flag = false
            }
            return newV
        })
        if (flag) break;
        i++
    }
    return i
}