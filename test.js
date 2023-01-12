function solution(A) {
  categorizedNums = {
    _getKey: (numVal) => {
      strNum = `${numVal}`
      return strNum[0] + strNum[strNum.length-1]
    },
    add: (value) => {
      const key = categorizedNums._getKey
      console.log(this)
      if (key in categorizedNums) {
        categorizedNums[key].push(value)
      } else {
        categorizedNums[key] = [value]
      }
    }
  }
  
  const getKeyFromFirstAndLastDigit = (number) => {
    strNum = `${number}`
    return strNum[0] + strNum[strNum.length-1]
  }

  A.forEach(el => {
    // const key = getKeyFromFirstAndLastDigit(el)
    categorizedNums.add(el)
  })

  maxSum = -1

  for (const key in categorizedNums) {
    const set = categorizedNums[key]
    for (const nums of combinations(set, 2)) {
      _sum = sumArr(nums)
      if (_sum > maxSum) {
        maxSum = _sum
      }
    }
  }
  return maxSum
}

const sumArr = (arr) => {
  return arr.reduce((acc, cur) => acc+cur, 0)
}

function* combinations (l, k) {
  if (k < 1) return yield []
  if (!Array.isArray(l)) {
    l = Array.from(l)  
  }
  for (let [i, x] of l.entries())
    for (let set of combinations([...l.slice(i + 1)], k - 1))
      yield [x, ...set]
}

arr = [130, 191, 200, 10]
arr = [11, 101, 1001]
// arr=[50, 222, 49, 52, 25]
res = solution(arr)
console.log(res)