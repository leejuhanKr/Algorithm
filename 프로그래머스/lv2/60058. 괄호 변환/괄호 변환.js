function solution(p) {
  if (p === '') return ''

  const [u, v] = seperate(p)

  return check(u)
    ? u + solution(v)
    : '(' + solution(v) + ')' + reverse(u.slice(1, -1))
}

const seperate = p => {
  idx = 0
  sum = 0
  do {
    sum += { '(': 1, ')': -1 }[p[idx++]]
  } while (sum !== 0)

  return [p.slice(0, idx), p.slice(idx)]
}

const check = p => {
  idx = 0
  sum = 0
  for (let c of p) {
    sum += { '(': 1, ')': -1 }[p[idx++]]
    if (sum < 0) return false
  }
  return true
}

const reverse = p =>
  p.split('').reduce((acc, cur) => acc + { '(': ')', ')': '(' }[cur], '')