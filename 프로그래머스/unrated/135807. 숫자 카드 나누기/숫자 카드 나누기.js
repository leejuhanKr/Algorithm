const _gcd = (a, b) => (b ? _gcd(b, a % b) : a)

const check = (arrA, arrB) => {
  g = arrA.reduce((acc, cur) => _gcd(acc, cur))
  for (let n = g; n > 0; n--) {
    if (g % n == 0 && arrB.every(v => v % n)) return n
  }
  return 0
}

const solution = (arrayA, arrayB) =>
  Math.max(check(arrayA, arrayB), check(arrayB, arrayA))