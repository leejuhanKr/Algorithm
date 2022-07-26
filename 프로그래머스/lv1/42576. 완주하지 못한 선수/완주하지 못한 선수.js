function solution(participant, completion) {
  // const table = participant.reduce(
  //   (acc, cur) => ({ ...acc, [cur]: (acc[cur] || 0) + 1 }),
  //   {}
  // );
    let person={}
    for (let i of participant){
        if(typeof person[i]==="undefined"){
             person[i] = 1
        }else{ //동명이인 있을 수 있어
            person[i]+=1
        }
    }
    table = person

  completion.forEach((p) => {
    table[p] -= 1;
  });

  for ([name, isRemain] of Object.entries(table)) {
    if (isRemain) return name;
  }
}