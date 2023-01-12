function solution(info, query) {
  const applicants = new Applicants()
  
  info
  .map(data => data.split(' '))
  .forEach(([lang, field, carrer, food, score]) => {
    applicants.append([lang, field, carrer, food], Number(score))
  })
  
  applicants.sortScores()

  return query
  .map(data => data.split(/ and | /))
  .forEach(([lang, field, carrer, food, score]) => {
    applicants
    .filter([lang, field, carrer, food])
    .take(score)
    .reduce((a,b)=>a+b,0)
  })
}

class Applicants {
  constructor(){
    this.data = new Map()
  }
  // append(params, val) {
  //   this.data.set(params, val)
  // }
  get(params){
    for (params)
  }
}

const tuple=(a,b)=>{
  fasd
}