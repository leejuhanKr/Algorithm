function solution(n) {
    return hanoi(n, 1, 2, 3)
}

function hanoi(n, init, base, target) {
    if (n===1) return [[init, target]]
    
    return [
        ...hanoi(n-1, init, target, base),
        [init, target],
        ...hanoi(n-1, base, init, target)
    ]
}