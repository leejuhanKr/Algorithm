function solution(begin, end) {
    res = []
    if (begin === 1) {
        res.push(0)
        begin += 1
    }
    for (let i = begin; i <= end; i++) {
        res.push(getLargestDivisorExceptSelf(i))
    }
    return res
}

const getLargestDivisorExceptSelf = (num) => {
    let start = 2
    if (num >= 20000000) {
        start = Math.ceil((num+1)/10000000)
    }
    for (let i = start; i<=num**0.5; i++) {
        if (num%i === 0) {
            return num/i
        }
    }
    return 1
}