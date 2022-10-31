from collections import namedtuple

def solution(keyinput, board):
    Key = namedtuple('Key',['up', 'down', 'left', 'right'])
    key = Key((0,1),(0,-1),(-1,0),(1,0))
    
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(x=(board[0]//2), y=(board[1]//2))
    
    for k in keyinput:
        dx, dy = getattr(key, k)
        x, y = p
        nx, ny = x+dx, y+dy
        if 0 <= nx < board[0]:
            p = p._replace(x = nx)
        if 0 <= ny < board[1]:
            p = p._replace(y = ny)
    return [p.x - (board[0]//2), p.y - (board[1]//2)]
    