function solution(land) {
    for (let i = 1; i < land.length; i++) {
        for (let j = 0; j < 4; j++) {
            land[i][j] += Math.max(...land[i-1].filter((_,k) => j != k))
        }
    }
    return Math.max(...land.at(-1))
}