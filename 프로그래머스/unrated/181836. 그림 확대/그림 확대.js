function solution(picture, k) {
    return [
        ...repeatArr(
        picture.map(row => [...repeatArr(row,k)].join('')),
        k)]
}

function* repeatArr(arr,n) {
    for (let i=0; i<arr.length; i++) {
        for (let j=0; j<n; j++) {
            yield arr[i]            
        }
    }
}