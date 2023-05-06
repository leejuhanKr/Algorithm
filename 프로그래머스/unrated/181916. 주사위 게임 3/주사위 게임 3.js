function solution(a, b, c, d) {
    const counted = count(a,b,c,d)

    return getScore(counted)
}

    
function count(...nums) {
    const res = {}
    for (const num of nums) {
        if (num in res) {
            res[num] += 1
        } else {
            res[num] = 1
        }
    }
    return res
}

function getScore(counted) {
    const arr = Object.entries(counted)
        .map(([num,cnt]) => [Number(num), cnt])
    arr.sort((a,b) => b[1]-a[1])
    const [p,q,r,s] = arr.map(el => el[0])

    if (arr.length === 1) {
        return scoreFromType1(p)
    }
    if (arr.length === 4) {
        return scoreFromType5(p,q,r,s)
    }
    if (arr.length === 3) {
        return scoreFromType4(q,r)
    }
    if (arr.length == 2) {
        if (arr[0][1] == 2) {
            return scoreFromType3(p,q)
        } else {
            return scoreFromType2(p,q)
        }
    }
}

const scoreFromType1 = (p) => 1111*p
const scoreFromType2 = (p, q) => ((10 * p) + q)**2
const scoreFromType3 = (p, q) => (p+q)*Math.abs(p-q)
const scoreFromType4 = (q, r) => q*r
const scoreFromType5 = (p, q, r, s) => Math.min(p,q,r,s)
