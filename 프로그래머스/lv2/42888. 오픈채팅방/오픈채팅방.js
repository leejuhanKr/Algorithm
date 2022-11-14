function solution(records) {
  users = {} // key: uid, val:nickname
  logs = [] // el:[uid, state]
  for (let record of records) {
    const [state, id, username] = record.split(' ')
    switch (state) {
      case 'Enter':
        if (!(id in users) || users[id] !== username) {
          users[id] = username
        }
        logs.push([id, 1])
        break
      case 'Leave':
        logs.push([id, 0])
        break
      case 'Change':
        users[id] = username
        break
    }
  }

  return logs.map(
    ([id, isEnterState]) =>
      `${users[id]}님이 ${isEnterState ? '들어왔' : '나갔'}습니다.`,
  )
}