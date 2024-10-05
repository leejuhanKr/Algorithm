function solution(m, n, startX, startY, balls) {
  return balls.map(ball=> {
      return Math.min(...minDist([startX, startY], ball, m, n))
  })
}

const minDist = (pos1, pos2, m, n) => {
  const [x1, y1] = pos1;
  const [x2, y2] = pos2;

  if (x1 === x2) {
    if (y1 < y2) {
      return ['t', 'l', 'r'].map((d) => getVP(pos1, m, n, d)).map((vp) => dist(...vp, ...pos2));
    } else {
      return ['b', 'l', 'r'].map((d) => getVP(pos1, m, n, d)).map((vp) => dist(...vp, ...pos2));
    }
  }
  if (y1 === y2) {
    if (x1 < x2) {
      return ['l', 't', 'b'].map((d) => getVP(pos1, m, n, d)).map((vp) => dist(...vp, ...pos2));
    } else {
      return ['r', 't', 'b'].map((d) => getVP(pos1, m, n, d)).map((vp) => dist(...vp, ...pos2));
    }
  }
  return ['l', 'r', 't', 'b'].map((d) => getVP(pos1, m, n, d)).map((vp) => dist(...vp, ...pos2));
};

const getVP = (pos, m, n, d) => {
  const [x, y] = pos;
  switch (d) {
    case 't':
      return [x, -y];
    case 'l':
      return [-x, y];
    case 'r':
      return [2 * m - x, y];
    case 'b':
      return [x, 2 * n - y];
  }
  throw new Error('check d')
};

const dist = (x1, y1, x2, y2) => {
  return ((x2 - x1) ** 2 + (y2 - y1) ** 2);
};
