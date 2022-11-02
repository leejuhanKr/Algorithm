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
    getVariants() {
        return Object.keys(this.cnt).length
    }
}