def solution(orders):
    stack = []
    res = 0
    i=0
    for b in range(len(orders)+1):
        stack.append(b)
        while stack[-1] == orders[i]:
            stack.pop()
            i += i < len(orders)-1
            res+=1
    return res
        
        
    

        