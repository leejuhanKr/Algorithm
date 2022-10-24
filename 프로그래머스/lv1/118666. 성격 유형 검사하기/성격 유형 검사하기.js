function* zip(...arr) {
  for (let i = 0; i < arr[0].length; i++) {
    yield arr.map((el) => el[i]);
  }
}

function solution(survey, choices) {
  const data = {};
  const types = ["RT", "CF", "JM", "AN"];
  for (type of types) {
    data[type] = 0;
  }
  for ([type, score] of zip(survey, choices)) {
    if (type[0] < type[1]) {
      data[type] += score - 4;
    } else {
      data[type[1] + type[0]] -= score - 4;
    }
  }

  return types.map((el) => (data[el] <= 0 ? el[0] : el[1])).join("");
}