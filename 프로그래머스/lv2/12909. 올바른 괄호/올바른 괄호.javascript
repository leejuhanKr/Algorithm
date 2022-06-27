function solution(s){
    let stack = [];
    for (const bracket of s) {
        if (bracket === '(') {
            stack.push('(');
        } else {
            if (!stack.length) return false
            stack.pop()
        }
    }
    return stack.length === 0;
}