function solution(topping) {
    part1 = new Counter(topping)
    part2 = new Counter()
    res = 0
    for (let el of topping) {
        part1.remove(el)
        part2.add(el)
        if (part1.length === part2.length) {
            res += 1
        }
    }
    return res
}

class Counter {
    constructor(arr = []) {
        this.cnt = {}
        this.length = 0
        arr.forEach(el => this.add(el))
    }
    add(el) {
        if (el in this.cnt) {
            this.cnt[el] += 1
        } else {
            this.cnt[el] = 1
            this.length += 1
        }
    }
    remove(el) {
        if (this.cnt[el] === 1) {
            delete this.cnt[el]
            this.length -= 1
        } else {
            this.cnt[el] -= 1
        }
    }
}

// function solution(topping) {
//     const [part1, part2] = [new Map(), new Map()]
//     topping.forEach(el => add(part1,el))
//     res = 0
    
//     for (let el of topping) {
//         add(part2,el)
//         remove(part1,el)
//         if (part1.size === part2.size) res += 1
//     }
    
//     return res
// }

// function add(part, el) {
//     if (tmp = part.get(el)) part.set(el, tmp+1)
//     else part.set(el, 1)
// }

// function remove(part, el) {
//     tmp = part.get(el)
//     if (tmp === 1) part.delete(el)
//     else part.set(el, tmp-1)
// }