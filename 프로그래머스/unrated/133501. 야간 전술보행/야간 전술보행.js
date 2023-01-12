function solution(distance, scopes, times) {
    // res = distance
    // scopes.forEach((v,i) => {
    //     const [w,r] = times[i]
    //     const [s,e] = v.sort((a,b)=> a-b)
    //     for (let d = s; d<=e; d++) {
    //         if ((d-1)%(w+r) < w) {
    //             res = Math.min(res,d)
    //         }
    //     }
    // })
    // return res
    return scopes.reduce((acc,cur,i) => {
        const [w,r] = times[i]
        const [s,e] = cur.sort((a,b)=> a-Math.min(acc,b))
        // const _e = Math.min(e, acc)
        console.log(s,e)
        for (let d = s; d<=e; d++) {
            if ((d-1)%(w+r) < w) {
                return Math.min(acc,d)
            }
        }
        return acc
    }, distance)
}