const getIdx = (arr, tmpIdx, load) => {
  for (let i = tmpIdx; i > 0; i--) {
    if (arr[i] === 0) continue;
    if (arr[i] < load) {
      load -= arr[i];
      arr[i] = 0;
    } else {
      arr[i] -= load;
      load = 0;
      if (arr[i] !== 0) return i;
    }
  }
  return 0;
};

function solution(cap, n, deliveries, pickups) {
  deliveries = [0].concat(deliveries);
  pickups = [0].concat(pickups);

  let a = getIdx(deliveries, n, 0);
  let b = getIdx(pickups, n, 0);
  let sum = 0;
  while (a || b) {
    sum += Math.max(a, b);
    if (a) {
      a = getIdx(deliveries, a, cap);
    }
    if (b) {
      b = getIdx(pickups, b, cap);
    }
  }
  return sum * 2;
}

console.log(solution(cap, n, deliveries, pickups));
