function* combination(arr, n) {
  if (n == 1) {
    yield* arr.map((v) => [v]);
    return;
  }
  for (let i = 0; i < arr.length; i++) {
    for (let rest of combination(arr.slice(i + 1), n - 1)) {
      yield [arr[i], ...rest];
    }
  }
}

function solution(orders, course) {
  res = [];
  for (let n of course) {
    sets = {}
    for (let [a, b] of combination(orders, 2)) {
      set = a.split("").filter((v) => b.split("").includes(v)).sort();
      for (let candiate of combination(set, n)) {
        key = candiate.join("");
        if (!sets[key]) {
          sets[key] = 1;
        } else {
          sets[key] += 1;
        }
      }
    }

    _max = Object.entries(sets).reduce((acc,cur) => {
      if (cur[1] > acc[1]) {
        return [[cur[0]], cur[1]]
      } else if (cur[1] == acc[1]) {
        return [[cur[0], ...acc[0]], acc[1]]
      }
      return acc
    }, [[],-Infinity])
    res = res.concat(_max[0])
  }
  return res.sort()
}