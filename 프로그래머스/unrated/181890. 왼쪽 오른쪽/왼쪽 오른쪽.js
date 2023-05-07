function solution(str_list) {
    lIdx = str_list.indexOf('l')
    rIdx = str_list.indexOf('r')

    if (lIdx===-1 && rIdx===-1) return []
    if (lIdx===-1) return str_list.slice(rIdx+1, str_list.length)
    if (rIdx===-1) return str_list.slice(0, lIdx)
    
    
    if (lIdx < rIdx) return str_list.slice(0, lIdx)
    else return str_list.slice(rIdx+1, str_list.length)
}