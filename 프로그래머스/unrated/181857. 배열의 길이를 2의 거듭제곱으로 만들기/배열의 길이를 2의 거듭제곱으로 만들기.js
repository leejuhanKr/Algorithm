function solution(arr) {
    n = 0
    while (2**n < arr.length) {
        n++
    }
    for (let i = arr.length; i < 2**n; i++) {
        arr[i] = 0
    }
    return arr
}
