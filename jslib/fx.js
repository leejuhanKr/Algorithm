const curry = f => (a, ...bs) => bs.length ? f(a, ...bs) : (...bs) => f(a, ...bs)

// const go = (...as) => reduce((a, f) => f(a), as)

const ago = (a, f) => a instanceof Promise ? a.then(f) : f(a)
const go = (...as) => reduce(ago, as)


/* 
Lazy
*/

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

L.take = curry(function *(length, iter) {
  let i = 0
  for (const a of iter) {
    if (i++ >= length) break
    yield a
  }
})

L.flat = function *(iter) {
  for (const a of iter) {
    if (a && a[Symbol.iterator]) yield *a
    else yield a
  }
}

/* 
Non Lazy
*/

const take = curry(function(length, iter) {
  let res = []
  for (const a of iter) {
    if (res.length == length) return res
    res.push(a)
  }
  return res
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

/* Test */


const add = curry((a, b) => a + b)

const f = (list, length) => go(
  list,
  L.filter(a => a % 2),
  L.map(a => a * a),
  L.take(length),
  reduce(add)
)

function main () {
const log = (x) => console.log(x) || x
// {
//   list = [1,2,3,4,5]
  
//   log(f(list, 1))
//   log(f(list, 2))
//   log(f(list, 3))
//   log(f(L.range(Infinity), 200))
// }
{
  const arr = [
    [1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [9, 10]
  ]
  res = go(
    arr,
    L.flat,
    L.filter(a => a % 2),
    L.map(a => (a * a)),
    L.take(3),
    reduce(add),
    // Array.from
  )
  res
}
{
  const users = [
    { name: 'a', age: 21, family: [
      { name: 'a1', age: 53 }, { name: 'a2', age: 47 },
      { name: 'a3', age: 16 }, { name: 'a4', age: 14 }
    ] },
    { name: 'b', age: 24, family: [
      { name: 'b1', age: 58 }, { name: 'b2', age: 51 },
      { name: 'b3', age: 10 }, { name: 'b4', age: 22 }
    ] },
    { name: 'c', age: 31, family: [
      { name: 'c1', age: 64 }, { name: 'c2', age: 62 }
    ] },
    { name: 'd', age: 20, family: [
      { name: 'd1', age: 42 }, { name: 'd2', age: 42 },
      { name: 'd3', age: 11 }, { name: 'd4', age: 7 }
    ] }
  ]

  const res = go(
    users,
    L.map(user => user.family),
    L.flat,
    L.filter(user => user.age < 20),
    L.map(user => user.age),
    L.take(3),
    reduce(add),
    // Array.from
  )
  res
}
/* monad, promise */
{
  // Compistion
  // f.g
  // f(g(x)) = f(g(x))
  let g = a => a + 1
  let f = a => a * a

  res = log(f(g(1)))

  // f(g(x)) = [] when g(x) -> error
  res =[1].map(g).map(f).map(log)

  // Kleisli Compostition, Promise
  // f(g(x)) = g(x) when g(x) -> error

  // case1
  res = Promise.resolve(1).then(g).then(f).then(log)
  res

  // case2
  g = JSON.parse
  f = ({k}) => k 
  const fg = x => Promise.resolve(x)
    .then(g)
    .then(f)
  
  res = fg('{"k": 10}').then(log)
  res
}
const delay = (ms, a) => new Promise(resolve =>
  setTimeout(() => resolve(a), ms))
{

  res = delay(100, 5).then(log)
  res instanceof Promise
  if (true) res.then(log)
}

/* go1 */
const go1 = (a, f) => a instanceof Promise ? a.then(f) : f(a)
{
  const a = 10
  const b = delay(1000, 5)

  res = go1(a, log)
  res = go1(b, log)
  
  res = go(Promise.resolve(1),
    a => a + 1,
    a => delay(100, a+3),
    log
  )

  async function af() {
    const b = await go(Promise.resolve(1),
    a => a + 1,
    a => delay(100, a+3),
    a => delay(100, a+4))
    
    const c = await go(Promise.resolve(1),
    a => a + 1,
    a => delay(100, a+3),
    a => delay(100, a+4))

    return log(a, b)
  }

  res = af()
  res
}
}

main()