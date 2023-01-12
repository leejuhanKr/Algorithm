const users = [[40,10000],[25,10000]]
const emoticons = [7000, 9000]
// result = [1, 5400]


// if discount = 40
let discount = 40
let user = users[0]
let earn = 0
let subscribe = 0
for (let emoticon of emoticons) {
  if (user[0] <= discount) {
    earn += emoticon * (100-discount) / 100 
  }
}
earn
