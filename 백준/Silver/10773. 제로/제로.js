const input = require("fs")
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split("\n");

ans = solution(input.slice(1).map(Number))
console.log(ans)

function solution(numArr){
  let stack = [];
  for (const num of numArr) {
      if (num != 0) {
          stack.push(num)
          continue
      }
      stack.pop()
  }
  return stack
    .reduce((acc, cur) => acc+cur, 0);
}