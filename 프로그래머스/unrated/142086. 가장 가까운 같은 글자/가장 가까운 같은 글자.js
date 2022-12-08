function solution(s) {
    const res = s.split('').map((v,i,arr) => {
        const findIdx = arr.lastIndexOf(v,i-1)
        return findIdx === -1 ? findIdx : i-findIdx
    })
    res.splice(0,1,-1)
    return res
}