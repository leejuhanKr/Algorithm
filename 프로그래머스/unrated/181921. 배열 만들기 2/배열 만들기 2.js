function solution(l, r) {
    const res = []
    for (const n of gen5Num()) {
        if (n < l) continue
        if (n > r) break
        res.push(n)
    }
    return res.length ? res : [-1]
}

function* gen5Num(l,r) {
    base=0
    while (true) {
        yield +(++base)
            .toString(2)
            .split('')
            .map(v => v==='1'?'5':'0')
            .join('')
    }
}