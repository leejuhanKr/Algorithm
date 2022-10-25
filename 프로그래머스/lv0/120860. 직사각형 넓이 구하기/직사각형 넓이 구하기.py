def solution(dots):
    [x1,*_,x2],[y1,*_,y2] = map(sorted, zip(*dots))
    return (x2-x1)*(y2-y1)