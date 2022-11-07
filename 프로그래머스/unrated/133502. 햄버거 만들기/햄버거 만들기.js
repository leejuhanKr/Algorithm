function solution(ingredient) {
    let stack = []
    const burger = [1,2,3,1]
    ingredient.forEach(v => {
        stack.push(v)
        if (burger.every((v,i) => stack.at(-4+i) === v)) {
            burger.forEach(() => stack.pop())
        }
    })
    return (ingredient.length-stack.length)/4
}
// function solution(ingredient) {
    
// }