function solution(s) {
    var answer = '';
    let words = s.split(' ');
    for (const word of words) {
        changedWord = ''
        for (const [i,c] of Object.entries(word)) {
            if (!(i%2)) {
                changedWord += c.toUpperCase()
            } else {
                changedWord += c.toLowerCase()
            }
        }
        answer += changedWord + ' '
    }
    return answer.slice(0,-1)
}