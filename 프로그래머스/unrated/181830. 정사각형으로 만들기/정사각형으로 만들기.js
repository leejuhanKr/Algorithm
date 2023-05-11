function solution(arr) {
    const rowLen = arr.length
    const colLen = arr[0].length
    
    if (rowLen < colLen) {
        fill = []
        for (let i=0; i<colLen; i++) {
            fill.push(0)
        }
        for (let i=0; i<colLen-rowLen; i++) {
            arr.push(fill)
        }
    }
        
    diff = rowLen-colLen
    for (const row of arr) {
        for (let i=0; i<diff; i++) {
            row.push(0)
        }
    }
    return arr
}