def solution(food, res = '0'):
    return solution(food, res.center(len(res)+(food.pop())//2*2,str(len(food)))) if food else res
    

    
    
        