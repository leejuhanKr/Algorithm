function solution(k, ranges) {
    const ks = []
    let nk
    while (k !== 1) {
        nk = k%2===0 ? k/2: k*3+1
        ks.push((k+nk)/2)
        k = nk
    }

    return ranges.map(([s,e]) => 
        s<=ks.length+e
        ? ks.slice(s,ks.length+e).reduce((a,b) => a+b,0)
        : -1
    )
}
