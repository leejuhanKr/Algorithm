function solution(n, words) {
    const used = new Set()
    let prev = words[0]
    used.add(prev)
    for (i = 1; i<words.length; i++) {
        tmp = words[i]
        if (used.has(tmp) || prev.at(-1) !== tmp.at(0)) {
            console.log(i)
            return [(i%n)+1, Math.floor(i/n)+1]
        }
        used.add(tmp)
        prev = tmp
    }
    return [0,0]
}