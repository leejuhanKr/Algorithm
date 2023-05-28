function solution(strArr) {
    const dict = {}
    for (const s of strArr) {
        _len = s.length
        if (dict[_len] === undefined) {
            dict[_len] = 0
        }
        dict[_len]+=1
    }
    
    _max = 0
    for (d in dict) {
        if (dict[d] > _max) {
            _max = dict[d]
        }
    }
    return _max
}