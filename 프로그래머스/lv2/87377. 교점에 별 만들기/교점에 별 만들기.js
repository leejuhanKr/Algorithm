function solution(line) {
  let points = []

  let maxX = -Number.MAX_VALUE
  let maxY = -Number.MAX_VALUE
  let minX = Number.MAX_VALUE
  let minY = Number.MAX_VALUE

  line.forEach((l1,i) => {
    let [a,b,e] = l1;
    line.slice(i+1).forEach((l2) => {
      let [c,d,f] = l2;

      let divider = a*d-b*c;
      if (divider === 0) return

      let [x,y] = [(b*f-e*d)/divider , (e*c-a*f)/divider]
      if (!(Number.isInteger(x) && Number.isInteger(y))) return

      points.push([x,y])
      maxX = Math.max(maxX,x)
      minX = Math.min(minX,x)
      maxY = Math.max(maxY,y)
      minY = Math.min(minY,y)
    })
  });

  let points_map = new Array(maxY-minY+1)
    .fill(0)
    .map(() => new Array(maxX-minX+1).fill('.'))
  console.log(points_map)

  points = points.map(([x,y]) => {
    console.log(x,y)
    return [maxY-y, x-minX]
  })
  console.log(points)

  points.forEach(([x,y])=>{
    points_map[x][y] = "*"
  })

  return points_map.map(arr => arr.join(''))
}