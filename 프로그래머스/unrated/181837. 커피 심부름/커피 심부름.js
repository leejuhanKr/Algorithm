function solution(order) {
    return order.map(v => {
        return v.match('cafelatte')?5000:4500
    }).reduce((acc,cur) => acc+cur)
}