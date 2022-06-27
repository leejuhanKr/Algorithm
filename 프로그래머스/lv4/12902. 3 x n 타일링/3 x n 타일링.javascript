function solution(n) {
  if (n&1) return 0;

  let [a,b] = [1,0]
  for (let i = 0; i<n; i=i+2) {
      [a,b] = [a+b, a*2+b*3].map(v => v%1000000007)
  }
  return (a+b)%1000000007
}