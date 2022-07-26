function solution(clothes) {
  const variations = clothes.reduce(
    (acc, [_, cur]) => ({ ...acc, [cur]: (acc[cur] || 1) + 1 }),
    {}
  );
  return Object.values(variations).reduce((acc, cur) => acc * cur, 1) - 1;
}
