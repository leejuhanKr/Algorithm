function solution(strArr) {
    const res = []
    
    for (let i=0; i<strArr.length; i++) {
        const el = strArr[i]
        if (i%2) res.push(el.toUpperCase())
        else res.push(el.toLowerCase())
    }
    
    return res
}