function solution(arr, query) {
    query.forEach((v,i)=> {
            if (i%2) {
                arr = arr.slice(v, arr.length)
            } else {
                arr = arr.slice(0, v+1)
            }
        })
    return arr
}