const today = "2022.05.19";
const terms = ["A 6", "B 12", "C 3"];
const privacies = [
  "2021.05.02 A",
  "2021.07.01 B",
  "2022.02.19 C",
  "2022.02.20 C",
];

/* // convertStringToDate
const cstd = (str) => {
  const res = str.split(".").map((v) => +v);
  const [y, m, d] = res;
  return d - 1 + 28 * (m - 1 + 12 * (y - 2000));
};

// const a = terms
// .map(v=>v.split(' '))
// .map(([a,b])=>[a,+b])
// const b = Object.fromEntries(a)

const getLimitDate = (terms) => {
  const _terms = Object.fromEntries(
    terms.map((v) => v.split(" ")).map(([a, b]) => [a, +b])
  );
  return (date, type) => {
    return cstd(date) + (_terms[type])*28
  };
};

console.log(cstd(today))
console.log(getLimitDate(terms)("2021.05.02",'A'))
console.log(cstd("2021.05.02"));

const getLimitDateWithTerms = getLimitDate(terms)

const res = privacies
.map(v => v.split(' '))
.map(([a,b])=> getLimitDateWithTerms(a,b)<=cstd(today))
.reduce((acc,cur,i) => cur?[...acc,i+1]:acc,[])

res
 */

function solution(today, terms, privacies) {
  const getLimitDateWithTerms = getLimitDate(terms)
  
  return privacies
      .map(v => v.split(' '))
      .map(([a, b]) => getLimitDateWithTerms(a, b) <= cstd(today))
      .reduce((acc, cur, i) => cur ? [...acc, i + 1] : acc, [])
}

// convertStringToDate
const cstd = (str) => {
  const res = str.split(".").map((v) => +v);
  const [y, m, d] = res;
  return d - 1 + 28 * (m - 1 + 12 * (y - 2000));
};

const getLimitDate = (terms) => {
  const _terms = Object.fromEntries(
      terms.map((v) => v.split(" ")).map(([a, b]) => [a, +b])
  );
  return (date, type) => {
      return cstd(date) + (_terms[type]) * 28
  };
};

a = solution(today, terms, privacies)
a