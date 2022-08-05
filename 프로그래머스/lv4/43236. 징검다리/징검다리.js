function solution(distance, rocks, n) {
  rocks = rocks.sort((a, b) => a - b);
  rocks.push(distance);
  return  bisect_l(0, distance, check(rocks, n));
}
function bisect_l(l, r, cb) {
  while (l <= r) {
    mid = (l + r) >> 1;
    if (cb(mid)) l = mid + 1;
    else r = mid - 1;
  }
  return r;
}
function check(dists, n) {
  return (maxDist) => {
    let pos = 0;
    let cnt = n;
    for (let dist of dists) {
      if (dist - pos < maxDist) {
        cnt -= 1;
        if (cnt < 0) return false;
      } else pos = dist;
    }
    return true;
  };
}
/* 
거리의 최솟값들의 최댓값이 target 이상이면 true를 반환하는 함수 cb

target을 바위간 거리의 최솟값들 중 최댓값이라고 가정하고
지워야할 바위들을 지워나가다 보면
n을 초과하는 경우가 있다.
이 경우는 최댓값이 target 미만 false를 리턴
아닌 경우는 최댓값이 target 이상 true를 리턴
*/