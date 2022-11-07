function solution(ingredients) {
    const stack = []
    const burger = [1,2,3,1]
    ingredients.forEach(ingredient => {
        stack.push(ingredient)
        // if (burger.every((b,i) => stack.at(-4+i) === b)) {
        if (burger.every((b,i) => stack[stack.length-4+i] === b)) {
            // burger.forEach(() => stack.pop())
            stack.splice(-4, 4)
        }
    })
    return (ingredients.length-stack.length)/4
}
