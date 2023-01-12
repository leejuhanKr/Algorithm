function solution(k, m, score) {
  score = score.sort((a, b) => a - b)
  return Array
      .from(range(score.length % m, score.length, m), i => score[i])
      .reduce((a, b) => a + b, 0) * m
}

function* range(s, e, offset) {
  for (let i = s; i < e; i += offset) {
    yield i
  }
}