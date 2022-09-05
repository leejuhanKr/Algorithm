function solution(n, k) {
    return  n
        .toString(k)
        .split(/0+/)
        .map(Number)
        .filter(isPrime)
        .length
}

const isPrime = (m) => {
    if (m===0 || m===1) return false
    for (let i = 2; i<=Math.floor(m**0.5); i++) {
        if (m%i===0) return false
    }
    return true
}