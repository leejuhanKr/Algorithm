function solution(arr, queries) {
    queries.forEach((v,i) => {
        const [s, e, k] = v
        for (let i = s; i<=e; i++) {
            if (i%k === 0) {
                arr[i]+=1
            }
        }
    })
    return arr
}