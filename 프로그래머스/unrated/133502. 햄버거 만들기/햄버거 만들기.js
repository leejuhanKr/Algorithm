function solution(ingredients) {
    const stack = []
    const burger = [1,2,3,1]
    ingredients.forEach(ingredient => {
        stack.push(ingredient)
        if (burger.every((b,i) => stack.at(-4+i) === b)) {
        // if (burger.every((b,i) => stack.at(stack.length-4+i) === b)) {
            burger.forEach(() => stack.pop())
        }
    })
    return (ingredients.length-stack.length)/4
}
