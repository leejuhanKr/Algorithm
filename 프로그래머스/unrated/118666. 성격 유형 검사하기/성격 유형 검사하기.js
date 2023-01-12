function solution(survey, choices) {
    const res = Object.fromEntries('RTCFJMAN'.split('').map(el=>[el,0]))
    for (const [type, choice] of zip(survey, choices)) {
        res[type[1]] += choice-4   
    }
    return ['RT','CF','JM','AN']
        .map(el=> el[+((-res[el[0]]+res[el[1]])>0)]).join('')
    return res
}  

const zip = function*(...arrs) {
    for (let idx = 0; idx < arrs[0].length; idx++) {
        yield arrs.map(arr => arr[idx])
    }
}