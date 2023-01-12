arr = [
    [1,1,1,1,1,1,1,1],
    [0,1,1,1,1,1,1,1],
    [0,0,0,0,1,1,1,1],
    [0,1,0,0,1,1,1,1],
    [0,0,0,0,0,0,1,1],
    [0,0,0,0,0,0,0,1],
    [0,0,0,0,1,0,0,1],
    [0,0,0,0,1,1,1,1],
    ]

def solution(arr):
    answer = []
    return answer

def get_numbers(x,y,size,arr):
    x, y = x*size, y*size
    for r in range(x,x+size):
        for c in range(y, y+size):
            yield arr(r,c)

print(*get_numbers(0,0,4,arr))
