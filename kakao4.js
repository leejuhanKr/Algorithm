const sol = (number) => {
  let len = 2;
  let str = number.toString(2);

  while (len <= str.length) {
    len *= 2;
  }
  len -= 1;
  const valid = (str) => {
    arr = str;
    idx = (len - 1) / 2;
    flag = [false]
    let d = (idx + 1) / 2;
    if (arr[idx]==='0') {
      return false
    }
    const cond1 = arr.filter((v,i)=>i%2===0).every(v=> v==='0')
    if (cond1) return false
    const prob = (idx, d) => {
      if (d < 1) {
        return true;
      }
      if (arr[idx] === "1") {
        return prob(idx - d, d / 2) && prob(idx + d, d / 2);
      } else {
        return arr
          .slice(idx - 2*d + 1, idx + 2*d)
          .split("")
          .every((v) => v === "0");
      }
    };
    return prob(idx, d);
  };
  if (len===str.length) return +(valid(str))
  ans = valid(str.padEnd(len, "0")) || valid(str.padStart(len, "0"));
  return +ans
};

console.log(sol(9))