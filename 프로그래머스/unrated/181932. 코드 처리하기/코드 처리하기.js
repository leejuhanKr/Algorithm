function solution(code) {
    let ret = ''
    let mode = '0'
    for (const [idx, c] of enumerate(code)) {
        if (isModeChangeFlag(c)) {
            mode = switchMode(mode)
            continue
        }
        
        
        if (mode === '0') {
            if (idx % 2 === 0) {
                ret += c
            }
        } else if (mode === '1') {
            if (idx%2 !== 0) {
                ret += c
            }
        }
    }
    
    return ret || 'EMPTY'
}

const isModeChangeFlag = (v) => ['1'].includes(v)
const switchMode = (v) => v==='1'?'0':'1'

function* enumerate(iterable, idx=0){
    idx = idx??0
    for (const v of iterable) {
        yield [idx++, v]
    }
}