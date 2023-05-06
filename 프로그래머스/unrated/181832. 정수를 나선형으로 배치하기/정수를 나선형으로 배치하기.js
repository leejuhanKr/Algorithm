function solution(n) {
    const arr = Array.from(
        {length:n}, 
        () => Array.from({length:n}, () => null)
    )
    
    let initialIdx = {x:0, y:0}

    v = 0
    for (const [r,c] of genPos(n)) {
        arr[r][c] = ++v
    }
    return arr
}

function* genPos(n) {
    let [rMin, rMax, cMin, cMax] = [0, n-1, 0, n-1]
    while (rMin <= rMax && cMin <= cMax) {
        for (let c = cMin; c< cMax; c++) {
            yield [rMin, c]
        }
        rMin ++
        for (let r = cMin; r<= rMax; r++) {
            yield [r, cMax]
        }
        cMax--
        for (let c = cMax; c>=cMin; c--) {
            yield [rMax, c]
        }
        rMax--
        for (let r = rMax; r>=rMin; r--) {
            yield [r, cMin]
        }
        cMin++
    }
}
