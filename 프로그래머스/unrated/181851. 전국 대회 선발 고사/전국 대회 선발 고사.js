function solution(rank, attendance) {
    let idx = -1
    const attendanceRankArr = []
    for (const [r, a] of zip(rank, attendance)) {
        idx++
        if (!a) continue
        
        attendanceRankArr.push([r,idx])
    }
    
    attendanceRankArr.sort((a,b) => a[0]-b[0])
    const [a,b,c] = attendanceRankArr
    
    return 10000*a[1] + 100*b[1] + c[1]
    
}

function* enumerate(iterable) {
    let idx = 0
    for (const v of iterable) {
        yield [idx++, iterable]
    }
}

function* zip(iterable1, iterable2) {
    for (let idx=0; idx<iterable1.length; idx++) {
        yield [iterable1[idx], iterable2[idx]]
    }
}

