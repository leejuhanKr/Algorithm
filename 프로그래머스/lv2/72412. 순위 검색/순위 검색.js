function solution(infos, querys) {
  const db = {};
  infos
  .map(info => preprocessData(info))
  .forEach(data => appendDataToDb(db, data))
  
  SortDb(db)

  const res = []
  v = querys
  .map(query => preprocessQuery(query))
  .forEach(([params,score]) => {
    let pass = 0
    let re = new RegExp(`^${params.map(param=>param==='-'?'[a-z]*':param).join(',')}$`)
    getScoresArrWithQuery(db, re)
    .forEach(scores => {
      pass += checkScore(scores, score)
    })
    res.push(pass)
  })

  return res
}


function preprocessData(info) {
  const data = info.split(" ");
  const key = data.slice(0, data.length - 1).join(",");
  const score = Number(data[data.length - 1]);
  return [key, score];
}

function appendDataToDb(db, data) {
  const [key, score] = data;
  if (db.hasOwnProperty(key)) {
    db[key].push(score);
  } else {
    db[key] = [score];
  }
}

function SortDb(db) {
  for (let values of Object.values(db)) {
    values.sort((a,b)=>(a-b))
  }
}

function preprocessQuery(query) {
  const data = query.split(/ and | /)
  const params = data.slice(0, data.length - 1);
  const score = Number(data[data.length - 1]);
  return [params, score];
}

function getScoresArrWithQuery(db, re) {
  const res = []
  for (const [key, scores] of Object.entries(db)) {
    if (isCorrespond(key, re)) {
      res.push(scores)
    }
  }
  return res
}

function isCorrespond(key, re) {
  return re.test(key)
}

function checkScore(scores, score) {
  return scores.length - bisect_r(scores, cond(score))
  // return scores.filter(cond(score)).length
}

function cond (limit) {return (score) => {
  return score>=limit
}}

function bisect_r(arr,cb) {
  let [l,r] = [0, arr.length-1]
  while (l<=r) {
    let mid = Math.floor((l+r)/2)
    if (cb(arr[mid])) r = mid-1
    else l = mid+1
  }
  return l
}