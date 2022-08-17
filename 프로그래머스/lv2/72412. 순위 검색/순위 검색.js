function solution(info, query) {
  db = {};
  info
  .map(processData(/ /))
  .forEach((data) => append(db, data));

  Object.values(db)
  .forEach((scores) => scores.sort((a, b) => a - b));

  return query
  .map(processData(/ and | /))
  .map(({ k: param, v: minScore }) =>
    Object.keys(db)
      .filter(checkKey(param))
      .map((k) => db[k])
      .map(getPassedNumber(minScore))
      .reduce((a, b) => a + b, 0)
  );
}
const mask = {
  //lang
  cpp: "001", python: "010", java: "100",
  // job group
  backend: "001", frontend: "010",
  // carrer
  junior: "001", senior: "010",
  //food
  chicken: "001", pizza: "010",
  // escape
  "-": "111",
};
const convert = (arr) => {
  return arr.map((v) => mask[v]).join("");
};
function processData(re) {
  return (dataString) => {
    const data = dataString.split(re);
    return {
      k: parseInt(convert(data.slice(0, data.length - 1)), 2).toString(),
      v: Number(data[data.length - 1]),
    };
  };
}
function append(db, data) {
  const { k: key, v: score } = data;
  if (db.hasOwnProperty(key)) {
    db[key].push(score);
  } else {
    db[key] = [score];
  }
}
function checkKey(param) {
  param = Number(param);
  return (key) => {
    key = Number(key);
    return (key & param) === key;
  };
}

function getPassedNumber(minScore) {
  // return (scores) => scores.filter((v) => v >= minScore).length;
  return (scores) => {
    let [l, r, mid] = [0, scores.length - 1, 0];
    while (l <= r) {
      mid = Math.floor((l + r) / 2);
      if (minScore <= scores[mid]) {
        r = mid - 1;
      } else {
        l = mid + 1;
      }
    }
    return scores.length - l;
  };
}
