def solution(ingredient):
    res = 0
    stack = []
    for i in ingredient:
        if i == 1 and len(stack) >= 3 and stack[-3:] == [1,2,3]:
            for _ in range(3): stack.pop()
            res += 1
        else:
            stack.append(i)
    return res
            