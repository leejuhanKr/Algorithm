const log = console.log

const curry = f => (a, ...bs) => bs.length ? f(a, ...bs) : (...bs) => f(a, ...bs)

const L = {}

L.range = function *(stop) {
  let i = -1
  while (++i < stop) yield i
}

L.filter = curry(function *(f, list) {
  for (const a of list) {
    if (f(a)) yield a
  }
})

L.map = curry(function *(f, list) {
  for (const a of list) {
    yield f(a)
  }
})

const take = curry(function(length, iter) {
  let res = []
  for (const a of iter) {
    if (res.length == length) return res
    res.push(a)
  }
  return res
})

L.take = curry(function *(length, iter) {
  let i = 0
  for (const a of iter) {
    if (i++ >= length) break
    yield a
  }
})

const reduce = curry(function (f, acc, iter) {
  if (arguments.length == 2) {
    iter = acc[Symbol.iterator]()
    acc = iter.next().value
  }
  for (const a of iter) {
    acc = f(acc, a);
  }
  return acc
})


const add = curry((a, b) => a + b)

const go = (...as) => reduce((a, f) => f(a), as)


const f = (list, length) => go(
  list,
  L.filter(a => a % 2),
  L.map(a => a * a),
  L.take(length),
  reduce(add)
)

function main () {
  list = [1,2,3,4,5]
  
  log(f(list, 1))
  log(f(list, 2))
  log(f(list, 3))
  log(f(L.range(Infinity), 200))

  res = add(3)(4)
  const foo = curry(a => a)
  res = foo(3)

}

main()