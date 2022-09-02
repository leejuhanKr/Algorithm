function solution(n) {
  let [a, b] = [0, 1];
  if (n < 2) return [a, b][n];
  for (let i = 2; i <= n; i++) {
    [a, b] = [b, (a + b) % 1234567];
  }
  return b;
}