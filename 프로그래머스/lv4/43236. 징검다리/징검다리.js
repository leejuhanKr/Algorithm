function solution(distance, rocks, n) {
  rocks = rocks.sort((a,b) => a-b)
  rocks.push(distance)
  return bisect_l(0,distance,cb,rocks,n)
}

function cb(dists,n,maxDist) {
  let pos = 0
  for (let dist of dists) {
    if (dist-pos<maxDist) {
      n-=1
      if (n<0) return false
    }
    else pos = dist
  }
  return true
}

function bisect_l(l,r,cb,dists,n) {
  while (l<=r) {
    mid = (l+r)>>1
    if (cb(dists,n,mid)) {l = mid+1}
    else {r = mid-1}
  }
  return r
}