function solution(n, words) {
    cnt=1;
    words.push('_')
    let lastWord = words[0][0]
    const visited = new Set();
    for (let w of words) {
        if (visited.has(w)) break
        visited.add(w)
        if (lastWord[lastWord.length-1] !== w[0]) break
        cnt++
        lastWord = w
    }
    if (cnt===words.length) return [0,0]
    return [(cnt%n)||n,Math.ceil(cnt/n)]
}