function solution(q1, q2) {
  let res = sum(q1);
  const target = (res + sum(q2)) / 2;
  const arr = [...q1, ...q2];
  let [i, j] = [0, q1.length];
  let cnt = 0;

  while (j <= arr.length) {
    if (res < target) {
      res += arr[j++];
      cnt++;
    } else if (res > target) {
      res -= arr[i++];
      cnt++;
    } else {
      return cnt;
    }
  }
  return -1;
}
const sum = (arr) => arr.reduce((acc, cur) => acc + cur, 0);
