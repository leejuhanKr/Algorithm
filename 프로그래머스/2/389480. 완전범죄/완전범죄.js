function solution(info, n, m) {
  const len = info.length;
  
  // dp[i][a] = i번째 물건까지 처리했을 때, A가 a개 흔적을 남겼을 때 B의 최소 흔적
  const dp = Array(len + 1).fill(0)
    .map(() => Array(n).fill(Infinity));
  
  // 초기값: 0개 물건, A=0, B=0
  dp[0][0] = 0;
  
  // 각 물건에 대해
  for (let i = 0; i < len; i++) {
    for (let a = 0; a < n; a++) {
      if (dp[i][a] === Infinity) continue;
      
      const b = dp[i][a]; // 현재 B의 흔적
      
      // 선택 1: A가 i번째 물건을 훔침
      const nextA = a + info[i][0];
      if (nextA < n) { // A가 안 잡히는 범위
        dp[i + 1][nextA] = Math.min(dp[i + 1][nextA], b);
      }
      
      // 선택 2: B가 i번째 물건을 훔침
      const nextB = b + info[i][1];
      if (nextB < m) { // B가 안 잡히는 범위
        dp[i + 1][a] = Math.min(dp[i + 1][a], nextB);
      }
    }
  }
  
  // 모든 물건을 훔친 후, A의 최소 흔적 찾기
  let answer = -1;
  for (let a = 0; a < n; a++) {
    if (dp[len][a] < m) { // B도 안 잡히는 경우
      answer = a;
      break; // a가 작은 순서대로 확인하므로 첫 번째가 최소
    }
  }
  
  return answer;
}