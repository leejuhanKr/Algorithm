function solution(distance, scopes, times) {
    scopes = scopes.map(scope => scope.sort((a,b)=> a-b))
    console.log(scopes)
    res = distance
    scopes.forEach(([s,e],i) => {
        const [w,r] = times[i]
        for (let d = s; d<=e; d++) {
            if (0<d%(w+r) &&  d%(w+r) <= w) {
                res = Math.min(res,d)
            }
        }
    })
    return res
}