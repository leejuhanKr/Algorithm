function solution(t, p) {
    const numLen = p.length
    let num = Array.from({length: numLen-1}, (v,i)=>t[i]).join('')
    let res = 0
    for (let idx = numLen-1; idx < t.length; idx++) {
        num = num + t[idx]
        if (num <= p) res++
        num = num.slice(1)
    }
    return res
}