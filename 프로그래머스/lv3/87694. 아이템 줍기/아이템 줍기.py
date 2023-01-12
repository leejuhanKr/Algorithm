from itertools import repeat
def solution(rectangle, cX, cY, iX, iY):
    paths = {}
    for x1,y1,x2,y2 in rectangle:
        a = [
            (1,0,range(x1,x2),repeat(y1)),
            (0,1,repeat(x2),range(y1,y2)),
            (-1,0,range(x2,x1,-1),repeat(y2)),
            (0,-1,repeat(x1),range(y2,y1,-1))
        ]
        for dx,dy,x_range,y_range in a:
            for x,y in zip(x_range,y_range):
                nx, ny = x+dx , y+dy
                if (x,y) in paths:
                    _x, _y = paths[(x,y)]
                    if x1<=_x<=x2 and y1<=_y<=y2:
                        paths[(x,y)] = (nx,ny)
                else:
                    paths[(x,y)] = (nx,ny)
    res= []
    for s,e in [((cX,cY), (iX,iY)), ((iX,iY),(cX,cY))]:
        cnt=0
        while s!=e:
            s = paths[s]
            cnt+=1
        res.append(cnt)

    return min(res)

    
    

    