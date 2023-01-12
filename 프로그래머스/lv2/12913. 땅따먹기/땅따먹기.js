function solution(land) {
    const res = land.reduce((acc, cur, i) => {
        return cur.map((v,i) => v + Math.max(...acc.filter((_, j) => j!=i)))
    })
    return Math.max(...res)
}


// for (let i = 1; i < land.length; i++) {
//     for (let j = 0; j < 4; j++) {
//         land[i][j] += Math.max(...land[i-1].filter((_,k) => j != k))
//     }
// }
// return Math.max(...land.at(-1))