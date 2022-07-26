function solution(clothes) {
  const variations = {};
  clothes.forEach(([_, type]) => {
    if (typeof variations[type] === "undefined") {
      variations[type] = 1;
    } else {
      variations[type]++;
    }
  });

  return Object.values(variations)
    .reduce((acc, cur) => acc * (cur + 1), 1) - 1;
}

	