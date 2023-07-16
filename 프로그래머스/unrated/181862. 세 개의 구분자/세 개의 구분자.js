function solution(myStr) {
    res = [];
    for (let a of split(myStr, "b")) {
        for (let b of split(a, "a")) {
            for (let c of split(b, "c")) {
                res.push(c)
            }
        }
    }
    return res.length?res:['EMPTY']
}

function* split(str, sep) {
    const res = [];
    let w = ''
    for (let el of str) {
        if (el === sep) {
            if (w) yield w
            w=''
        } else {
            w += el
        }
    }
    if (w) yield w
}
    
    