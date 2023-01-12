function solution(n, words) {
    let prev = words[0]
    // const used = new Set([prev])
    
    // for (let [i,tmp] of Array.from(words.slice(1), (v,i) => [i+1,v])) {
    for (let i = 1; i<words.length; i++) {
        tmp = words[i]
        // if (used.has(tmp) || prev.at(-1) !== tmp.at(0)) {
        if (words.lastIndexOf(tmp,i-1)!==-1 || prev.at(-1) !== tmp.at(0)) {
            return [(i%n)+1, Math.floor(i/n)+1]
        }
        // used.add(tmp)
        prev = tmp
    }
    
    return [0,0]
}