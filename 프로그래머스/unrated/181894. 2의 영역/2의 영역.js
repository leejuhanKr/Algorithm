function solution(arr) {
    const startIdx = arr.indexOf(2)
    const endIdx = arr.lastIndexOf(2)
    
    const sliced = arr.slice(startIdx, endIdx+1)
    return sliced.length ? sliced : [-1]
}