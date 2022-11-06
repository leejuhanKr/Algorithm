function solution(babbling) {
    arr = ["aya", "ye", "woo", "ma"]
    return babbling.reduce((acc,cur) => acc+isValid(cur,arr), 0)
}

const isValid = (word, arr, prevIdx = -1, stringIdx = 0) => {
    l1: while (stringIdx < word.length) {
        for (let i = 0; i<arr.length; i++) {
            if (i!==prevIdx && word.startsWith(arr[i], stringIdx)) {
                stringIdx += arr[i].length
                prevIdx = i
                continue l1
            }
        }
        return false
    }
    return true
}