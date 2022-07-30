function solution(name) {
    return countShift(name) + countUpDown(name);
}

const countShift = (name) => {
    let cnt = name.length-1
    let i = 0
    while (i < name.length) {
        if (name[i+1]!=='A') {
            i++
            continue
        }
        
        let j = i
        do {j++} while (j < name.length && name[j]==='A')
        
        let left = i
        let right = name.length-j
        console.log(left, right)
        cnt = Math.min(cnt, 2*left+right, 2*right+left)
        i = j
    }
    return cnt
}

const countUpDown = (name) => {
    const countOneChar = (c) => {
        return Math.min(
            c.charCodeAt(0)-65, 
            91-c.charCodeAt(0)
        )
    }
    return name
        .split('')
        .reduce((acc,cur) => acc+countOneChar(cur)
               ,0)
}
    
