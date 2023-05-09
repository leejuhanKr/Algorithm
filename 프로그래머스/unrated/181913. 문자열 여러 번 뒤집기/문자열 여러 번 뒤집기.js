function solution(my_string, queries) {
    let arr = my_string.split('')
    queries.forEach(([s,e]) => {
        reverse = arr.slice(s,e+1).reverse()
        arr.splice(s,e-s+1,...reverse)
    })
    return arr.join('')
}